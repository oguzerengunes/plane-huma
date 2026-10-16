from django.urls import include, path
urlpatterns += [path("api/huma/", include("huma_policy.urls"))]
