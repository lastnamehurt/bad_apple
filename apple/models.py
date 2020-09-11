# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from incident.models import Incident


class BadApple(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    incidents = models.ManyToManyField(Incident)
    image = models.ImageField(default='')

    def __str__(self):
        return "<{}> {} {}".format(self.id, self.first_name, self.last_name)
