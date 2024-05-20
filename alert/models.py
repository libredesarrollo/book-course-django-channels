from django.db import models

from django.contrib.auth.models import User

class Alert(models.Model):
    content = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)    