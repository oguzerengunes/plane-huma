import uuid
from django.db import models
from django.utils import timezone


class DepartmentInviteCode(models.Model):
    """Departman davet kodu (ham kod DB'de saklanmaz)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_id = models.CharField(max_length=64, db_index=True)
    code_hash = models.CharField(max_length=64, unique=True)
    prefix = models.CharField(max_length=12, db_index=True)
    expires_at = models.DateTimeField()
    max_uses = models.PositiveIntegerField(default=1)
    use_count = models.PositiveIntegerField(default=0)
    require_approval = models.BooleanField(default=True)
    is_revoked = models.BooleanField(default=False)
    created_by = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["project_id", "is_revoked"]),
            models.Index(fields=["expires_at"]),
        ]

    def is_valid(self) -> bool:
        return not self.is_revoked and self.use_count < self.max_uses and self.expires_at > timezone.now()


class DepartmentJoinRequest(models.Model):
    """Kod ile katılım isteği."""
    class Status(models.TextChoices):
        PENDING = "pending", "Bekliyor"
        APPROVED = "approved", "Onaylandı"
        REJECTED = "rejected", "Reddedildi"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invite = models.ForeignKey(DepartmentInviteCode, on_delete=models.CASCADE, related_name="requests")
    project_id = models.CharField(max_length=64, db_index=True)
    user_id = models.CharField(max_length=64)
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    decided_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["invite", "user_id"], name="uniq_invite_user"),
        ]
        indexes = [models.Index(fields=["project_id", "status"])]
