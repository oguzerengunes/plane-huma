from django.contrib import admin
from .models import DepartmentInviteCode, DepartmentJoinRequest


@admin.register(DepartmentInviteCode)
class InviteCodeAdmin(admin.ModelAdmin):
    list_display = ("prefix", "project_id", "is_revoked", "expires_at", "use_count", "max_uses")


@admin.register(DepartmentJoinRequest)
class JoinRequestAdmin(admin.ModelAdmin):
    list_display = ("project_id", "user_id", "status", "created_at")
