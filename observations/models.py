# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from datetime import datetime
from django.contrib.auth.models import User


class Observations(models.Model):
    SYNC_TYPES = (
        ('E', 'E'),
        ('G', 'G'),
        ('F', 'F'),
        ('P', 'P')
    )
    sync = models.CharField(max_length=1, choices=SYNC_TYPES)
    groups = models.IntegerField(max_length=4)
    spots = models.IntegerField(max_length=4)
    wolf = models.IntegerField(max_length=4)
    remarks = models.CharField(max_length=200, blank=True)
    creation = models.DateTimeField(default=datetime.now)
    deleted = models.BooleanField(default=False)
    valid = models.BooleanField(default=True)
    user = models.ForeignKey(User)


class ObservationsForm(ModelForm):
    class Meta:
        model = Observations
        exclude = ('creation', 'deleted', 'user', 'valid', 'wolf')
