from django.db import transaction
from django.db.models import F
from django.utils import timezone
from rest_framework import permissions, throttling
from rest_framework.response import Response
from rest_framework.views import APIView
from . import adapter
from .models import DepartmentInviteCode, DepartmentJoinRequest
from .serializers import InviteCreateSerializer, JoinByCodeSerializer, JoinRequestListSerializer
from .utils import generate_code, hash_code, prefix_of, verify


class BurstThrottle(throttling.SimpleRateThrottle):
    scope = "burst"

    def get_cache_key(self, request, view):
        return self.get_ident(request)


class CreateInviteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        s = InviteCreateSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        code = generate_code()
        DepartmentInviteCode.objects.create(
            project_id=s.validated_data["project_id"],
            code_hash=hash_code(code),
            prefix=prefix_of(code),
            expires_at=timezone.now() + timezone.timedelta(hours=s.validated_data["ttl_hours"]),
            max_uses=s.validated_data["max_uses"],
            require_approval=s.validated_data["require_approval"],
            created_by=str(request.user.id),
        )
        return Response({"code": code}, status=201)


class JoinByCodeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        s = JoinByCodeSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        h, pid = hash_code(s.validated_data["code"]), s.validated_data["project_id"]
        with transaction.atomic():
            inv = DepartmentInviteCode.objects.select_for_update().filter(code_hash=h, project_id=pid).first()
            if not inv or not verify(s.validated_data["code"], inv.code_hash) or not inv.is_valid():
                return Response({"detail": "geçersiz kod"}, status=400)
            req, _ = DepartmentJoinRequest.objects.get_or_create(
                invite=inv, user_id=str(request.user.id), defaults={"project_id": pid}
            )
            if not inv.require_approval:
                adapter.join(pid, str(request.user.id))
                req.status = "approved"
                req.decided_at = timezone.now()
                req.save()
                DepartmentInviteCode.objects.filter(pk=inv.pk).update(use_count=F("use_count") + 1)
        return Response({"status": req.status})


class ListRequestsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, project_id):
        qs = DepartmentJoinRequest.objects.filter(project_id=project_id, status="pending")
        return Response(JoinRequestListSerializer(qs, many=True).data)


class ApproveView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        with transaction.atomic():
            req = DepartmentJoinRequest.objects.select_for_update().get(pk=pk)
            adapter.join(req.project_id, req.user_id)
            req.status = "approved"
            req.decided_at = timezone.now()
            req.save()
            DepartmentInviteCode.objects.filter(pk=req.invite_id).update(use_count=F("use_count") + 1)
        return Response({"status": "approved"})


class RejectView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        req = DepartmentJoinRequest.objects.get(pk=pk)
        req.status = "rejected"
        req.decided_at = timezone.now()
        req.save()
        return Response({"status": "rejected"})
