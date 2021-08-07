from django.db import models
from django.utils import timezone


class Post(models.Model):
    post_id = models.IntegerField()
    user_id = models.IntegerField()

class PostStatistics(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.IntegerField(null=True)
    likes_count = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
