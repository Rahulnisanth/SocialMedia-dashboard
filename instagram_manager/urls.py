from django.urls import path
from .views import *

urlpatterns = [
    path('link-instagram/<int:pk>/', create_instagram_user_access)
]
