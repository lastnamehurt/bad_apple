from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.user.username)
