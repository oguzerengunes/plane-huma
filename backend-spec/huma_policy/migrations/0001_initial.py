from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="DepartmentInviteCode",
            fields=[
                ("id", models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)),
                ("project_id", models.CharField(max_length=64, db_index=True)),
                ("code_hash", models.CharField(max_length=64, unique=True)),
                ("prefix", models.CharField(max_length=12, db_index=True)),
                ("expires_at", models.DateTimeField()),
                ("max_uses", models.PositiveIntegerField(default=1)),
                ("use_count", models.PositiveIntegerField(default=0)),
                ("require_approval", models.BooleanField(default=True)),
                ("is_revoked", models.BooleanField(default=False)),
                ("created_by", models.CharField(max_length=64)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"indexes": [models.Index(fields=["project_id", "is_revoked"]), models.Index(fields=["expires_at"])]},
        ),
        migrations.CreateModel(
            name="DepartmentJoinRequest",
            fields=[
                ("id", models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)),
                ("invite", models.ForeignKey(to="huma_policy.DepartmentInviteCode", on_delete=models.CASCADE, related_name="requests")),
                ("project_id", models.CharField(max_length=64, db_index=True)),
                ("user_id", models.CharField(max_length=64)),
                ("status", models.CharField(max_length=16, default="pending")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("decided_at", models.DateTimeField(null=True, blank=True)),
            ],
            options={"indexes": [models.Index(fields=["project_id", "status"])]},
        ),
        migrations.AddConstraint(
            model_name="departmentjoinrequest",
            constraint=models.UniqueConstraint(fields=["invite", "user_id"], name="uniq_invite_user"),
        ),
    ]
