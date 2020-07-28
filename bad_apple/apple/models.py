# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class BadApple(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    badge_number = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name, self.city, self.state
