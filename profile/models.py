# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class UserProfile(models.Model):
    GROUP_NAMES = (
        ('Observer', 'Observer'),
        ('Analyst', 'Analyst'),
        ('Admin', 'Admin'),
    )
    user = models.ForeignKey(User, unique=True)
    email = models.EmailField(max_length=100)
    aavsocode = models.CharField(max_length=4)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    postal = models.IntegerField(max_length=5)
    country = models.CharField(max_length=40)
    landline = models.CharField(max_length=14)
    mobile = models.CharField(max_length=14)
    creation_date = models.DateTimeField(default=datetime.now)
    groups = models.CharField(max_length=8, choices=GROUP_NAMES)
    valid = models.BooleanField()


class Equipment(models.Model):
    METHODS = (
        ('Projection', 'Projection'),
        ('Direct', 'Direct'),
        ('Drawing', 'Drawing'),
        ('Photo', 'Photo'),
        ('Visual', 'Visual'),
    )
    INSTRUMENTS = (
        ('Reflector', 'Reflector'),
        ('Refractor', 'Refractor'),
        ('SCT', 'SCT'),
        ('Maksutov', 'SCT/Maksutov'),
    )
    FOCAL_TYPES = (
        ('MM', 'MM (milimeters)'),
        ('D', 'D (diameter)'),
    )
    name = models.CharField(max_length=50)
    method = models.CharField(max_length=10, choices=METHODS)
    instrument = models.CharField(max_length=9, choices=INSTRUMENTS)
    aperture = models.DecimalField(max_digits=2, decimal_places=2)
    eyepiece = models.DecimalField(max_digits=2, decimal_places=2)
    magnification = models.IntegerField(max_length=3)
    focal_length = models.IntegerField(max_length=3)
    focal_length_type = models.CharField(max_length=2, choices=FOCAL_TYPES)
    filtr = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey('UserProfile')
