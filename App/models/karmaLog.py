# karmaLog.py
from django.db import models
from .user import User

class KarmaLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    change = models.IntegerField()
    action = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)