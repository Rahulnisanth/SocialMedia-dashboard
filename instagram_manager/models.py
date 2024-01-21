from django.db import models
import uuid


# Create your models here.
class Instagram(models.Model):
    user_id = models.CharField(max_length=350, blank=True, null=True)
    access_token = models.CharField(max_length=350, blank=True, null=True)
    password = models.CharField(max_length=350, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )

    def __str__(self):
        return str(self.user_id)


class Post(models.Model):
    user_id = models.ForeignKey(
        Instagram, null=True, blank=True, on_delete=models.CASCADE
    )
    post_name = models.CharField(max_length=350, blank=True, null=True)
    comments = models.IntegerField(default=0, null=True, blank=True)
    likes = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )

    def __str__(self):
        return str(self.post_name)


class Account(models.Model):
    user_id = models.ForeignKey(
        Instagram, null=True, blank=True, on_delete=models.CASCADE
    )
    followers = models.IntegerField(default=0, null=True, blank=True)
    followings = models.IntegerField(default=0, null=True, blank=True)
    media_count = models.IntegerField(default=0, null=True, blank=True)
    profile_url = models.CharField(max_length=250, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )

    def __str__(self):
        return str(self.user_id)
