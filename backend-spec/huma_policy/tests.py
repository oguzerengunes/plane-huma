from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from .models import DepartmentInviteCode, DepartmentJoinRequest
from .utils import generate_code, hash_code, verify


class PolicyAcceptanceTests(TestCase):
    def setUp(self):
        self.code = generate_code()
        self.inv = DepartmentInviteCode.objects.create(
            project_id="proj-1", code_hash=hash_code(self.code), prefix=self.code[:4],
            expires_at=timezone.now() + timedelta(hours=72), max_uses=5,
            require_approval=True, created_by="admin-1",
        )

    def test_hash_verify(self):
        self.assertTrue(verify(self.code, self.inv.code_hash))

    def test_pending_flow(self):
        r = DepartmentJoinRequest.objects.create(invite=self.inv, project_id="proj-1", user_id="u-1")
        self.assertEqual(r.status, "pending")

    def test_unique_per_user(self):
        DepartmentJoinRequest.objects.create(invite=self.inv, project_id="proj-1", user_id="u-2")
        with self.assertRaises(Exception):
            DepartmentJoinRequest.objects.create(invite=self.inv, project_id="proj-1", user_id="u-2")

    def test_expired_invalid(self):
        self.inv.expires_at = timezone.now() - timedelta(hours=1)
        self.assertFalse(self.inv.is_valid())

    def test_single_row(self):
        DepartmentJoinRequest.objects.create(invite=self.inv, project_id="proj-1", user_id="u-3")
        self.assertEqual(DepartmentJoinRequest.objects.filter(project_id="proj-1", user_id="u-3").count(), 1)
