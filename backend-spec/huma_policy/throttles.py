from rest_framework.throttling import UserRateThrottle


class JoinRateThrottle(UserRateThrottle):
    scope = "join"
    rate = "5/10m"

    def get_cache_key(self, request, view):
        if not request.user.is_authenticated:
            return self.get_ident(request)
        return f"throttle_join_{request.user.pk}"
