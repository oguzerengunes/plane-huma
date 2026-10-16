from rest_framework.permissions import BasePermission


class IsProjectAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        u = request.user
        if not u or not u.is_authenticated:
            return False
        if getattr(obj, "owner_id", None) == getattr(u, "id", None):
            return True
        try:
            return obj.memberships.filter(user=u, role="admin", is_active=True).exists()
        except Exception:
            return False
