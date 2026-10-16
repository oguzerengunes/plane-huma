"""Plane üyelik adaptörü. Direkt DB INSERT YASAK: tek yol bu wrapper."""
import logging

log = logging.getLogger(__name__)


def join(project_id: str, user_id: str, role: str = "member") -> dict:
    """Kullanıcıyı Plane projesine üye yap. Direkt INSERT yasak."""
    # Plane fork içinde: from plane.services import ProjectMemberService
    # return ProjectMemberService.add_member(project_id, user_id, role)
    log.info("plane.add_member project=%s user=%s", project_id, user_id)
    raise NotImplementedError("Plane fork içine kopyalayınca bağlayın")
