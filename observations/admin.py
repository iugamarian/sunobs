# -*- coding: utf-8 *-*
from django.contrib import admin
from sunobs.observations.models import Observations


class ObservationsAdmin(admin.ModelAdmin):
    list_display = ('sync', 'user',)
    list_filter = ('valid',)

admin.site.register(Observations, ObservationsAdmin)
