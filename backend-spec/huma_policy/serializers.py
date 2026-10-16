from rest_framework import serializers
from .models import DepartmentJoinRequest

# NOT: code_hash asla response'da expose edilmez.


class InviteCreateSerializer(serializers.Serializer):
    project_id = serializers.CharField(max_length=64)
    max_uses = serializers.IntegerField(min_value=1, max_value=1000, default=1)
    ttl_hours = serializers.IntegerField(min_value=1, max_value=720, default=72)
    require_approval = serializers.BooleanField(default=True)


class JoinByCodeSerializer(serializers.Serializer):
    code = serializers.CharField(min_length=10, max_length=64, write_only=True)
    project_id = serializers.CharField(max_length=64)


class JoinRequestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentJoinRequest
        fields = ["id", "project_id", "user_id", "status", "created_at", "decided_at"]
        read_only_fields = fields
