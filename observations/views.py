# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from sunobs.profiles.models import UserProfile
from sunobs.observations.models import Observations, ObservationsForm


def dashboard(request):
    if request.user.is_authenticated():
        try:
            me = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            return redirect('/register/')
        observations = Observations.objects.filter(user=me)
        return render(request, 'dashboard.html', locals())
    else:
        return redirect('/')


def o_view(request):
        return redirect('/')


def o_edit(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        form = ObservationsForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = user
            f.wolf = 10 * int(f.groups) + int(f.spots)
            form.save()
            return redirect('/dashboard/')
    else:
        form = ObservationsForm()
        return render(request, 'o_edit.html', locals())

