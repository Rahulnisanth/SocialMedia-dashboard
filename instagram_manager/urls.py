from django.urls import path
from .views import *

<<<<<<< HEAD
urlpatterns = [path("link-instagram/<int:pk>/", create_instagram_user_access)]
=======
urlpatterns = [
    path('link-instagram/<str:pk>', create_instagram_user_access, name='link-instagram')
]
>>>>>>> c06db0bd52ebb087f88ba58ffaefd41607e4fdf3
