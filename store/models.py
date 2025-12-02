from django.db import models

from django.contrib.auth.models import User

class Medicine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    available_stock = models.PositiveIntegerField(default=0)
    added_time = models.DateTimeField(auto_now_add=True)