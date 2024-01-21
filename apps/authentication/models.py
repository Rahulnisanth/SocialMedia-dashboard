from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        null=True,
        blank=True,
        default="static/assets/img/profile-cover.jpg",
        upload_to="media/profiles/",
    )
    firstname = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    email = models.CharField(null=True, blank=True, max_length=150, unique=True)
    short_intro = models.CharField(null=True, blank=True, max_length=1000)
    # ADDRESS MODULES...
    address = models.CharField(max_length=200, null=True, blank=True)
    number = models.BigIntegerField(default=0, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    code = models.IntegerField(default=000000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )

    def __str__(self):
        return str(self.user)
