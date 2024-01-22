from django.urls import path
from .views import *

urlpatterns = [
    path(
        "link-instagram/<str:pk>", create_instagram_user_access, name="link-instagram"
    ),
<<<<<<< HEAD
=======
    path("update/dashboard/instagram", fetch_data_from_account, name="update-data"),
    path("dashboard-instagram.html", create_instagram_user_access, name="update-data"),
>>>>>>> 9b7877d8693599f6e1896e6bb7e63efbcc053607
]
