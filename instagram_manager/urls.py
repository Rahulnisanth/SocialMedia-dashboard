from django.urls import path
from .views import *

urlpatterns = [
    path(
        "link-instagram/<str:pk>", create_instagram_user_access, name="link-instagram"
    ),
    path("update/dashboard/instagram", fetch_data_from_account, name="update-data"),
    path("dashboard-instagram.html", create_instagram_user_access, name="update-data"),
    path("delete/instagram-account/<str:pk>", delete_instagram_user_access, name="unlink-instagram-account"),
]
