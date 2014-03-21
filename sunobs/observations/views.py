# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from sunobs.observations.models import Observations, ObservationsForm

User = get_user_model()


@login_required
def dashboard(request):
    me = User.objects.get(email=request.user)
    observations = Observations.objects.filter(user=me)
    return render(request, 'dashboard.html', {'me': me,
                                              'observations': observations})


def o_view(request):
        return redirect('/')


@login_required
def o_edit(request):
    if request.method == 'POST':
        user = User.objects.get(email=request.user)
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
