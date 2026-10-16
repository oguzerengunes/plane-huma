from django.urls import path
from .views import ApproveView, CreateInviteView, JoinByCodeView, ListRequestsView, RejectView

urlpatterns = [
    path("invites/", CreateInviteView.as_view(), name="invite-create"),
    path("join/", JoinByCodeView.as_view(), name="join-by-code"),
    path("projects/<str:project_id>/requests/", ListRequestsView.as_view(), name="request-list"),
    path("requests/<uuid:pk>/approve/", ApproveView.as_view(), name="request-approve"),
    path("requests/<uuid:pk>/reject/", RejectView.as_view(), name="request-reject"),
]
