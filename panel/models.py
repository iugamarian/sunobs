# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Profile(models.Model):
    GROUP_NAMES = (
        ('O', 'Observer'),
        ('N', 'Analyst'),
        ('D', 'Admin'),
    )
    user = models.ForeignKey(User, unique=True)
    aavsocode = models.CharField(max_length=4, verbose_name="AAVSO Code")
    address = models.CharField(max_length=100, verbose_name="Address")
    city = models.CharField(max_length=40, verbose_name="City")
    postal = models.IntegerField(max_length=5, verbose_name="Postal Code")
    country = models.CharField(max_length=40, verbose_name="Country")
    landline = models.CharField(max_length=14, verbose_name="Landline")
    mobile = models.CharField(max_length=14, verbose_name="Mobile")
    creation_date = models.DateTimeField(default=datetime.now)
    groups = models.CharField(max_length=1, choices=GROUP_NAMES)
    valid = models.BooleanField()
