from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    content = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class Comment(models.Model):
    post=models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="comments"
    )
    content = models.TextField(max_length=200)

    def __str__(self):
        return self.content