from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path("admin/", admin.site.urls),  # Django admin route
    path("", include("apps.authentication.urls")),  # Auth routes - login / register
    path("", include("apps.home.urls")),  # UI Kits Html files
    path("", include("instagram_manager.urls")),  # UI Kits Html files
]
