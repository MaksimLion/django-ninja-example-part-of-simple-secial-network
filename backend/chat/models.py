from django.db import models
from users.models import User
from .querysets import DialogQuerySet


class Dialog(models.Model):
    users = models.ManyToManyField(User, related_name="dialogs")
    objects = DialogQuerySet.as_manager()


class Message(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_dialog = models.ForeignKey(Dialog, on_delete=models.CASCADE, related_name="messages")
    datetime = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    is_read = models.BooleanField(default=False)

