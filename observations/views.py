# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from sunoss.profile.models import UserProfile
from sunoss.observations.models import Observations, ObservationsForm


def me(request):
    if request.user.is_authenticated():
        try:
            me = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            return redirect('/register/')
        observations = Observations.objects.filter(user=me)
        return render(request, 'me.html', locals())
    else:
        return redirect('/')
