from django.urls import path
from .views import *

urlpatterns = [
    path(
        "link-instagram/<str:pk>", create_instagram_user_access, name="link-instagram"
    ),
]
