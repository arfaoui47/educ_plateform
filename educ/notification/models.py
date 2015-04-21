from django.db import models
from forum.models import User


class Notification(models.Model):
    contents = models.TextField()
    link = models.CharField(max_length=50)
    statement = models.BooleanField(default=0)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now=False,auto_now_add=True)

