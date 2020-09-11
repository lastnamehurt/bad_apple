# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Incident(models.Model):
    date = models.DateField(auto_now_add=False, null=True)
    summary = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipCode = models.CharField(max_length=10)
    # media = models.ImageField()
    reported_by = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    apple = models.ForeignKey('apple.BadApple', on_delete=models.CASCADE, null=True) # can be null in case a reporter
    # doesn't capture enough information to identify the BadApple. In this case users will rely on descriptions until
    # identified. Will support attaching a BadApple to an apple-less Incident!

    def __str__(self):
        return "{} | {}".format(self.date, self.apple)

    def context(self):
        data = {
            'date': self.date,
            'summary': self.summary,
            'details': self.details,
            'city': self.city,
            'state': self.state,
            'zipCode': self.zipCode,
            'reported_by': self.reported_by,
            'apple': self.apple,
        }
        return data
