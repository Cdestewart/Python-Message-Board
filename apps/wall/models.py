from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from ..first_app.models import User

class Message(models.Model):
    messages = models.TextField(max_length = 1000, default ="")
    poster = models.ForeignKey(User, related_name = "message_id", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    comments = models.TextField(max_length = 1000, default ="")
    message_id = models.ForeignKey(Message, related_name = "comment_id", on_delete=models.CASCADE)
    poster = models.ForeignKey(User, related_name = "comm_id", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)