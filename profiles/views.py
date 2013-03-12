# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from sunobs.profiles.models import UserProfile, UserProfileForm


def register(request):
    if request.user.is_authenticated():
        try:
            me = UserProfile.objects.get(user=request.user)
            return redirect('/dashboard/')
        except UserProfile.DoesNotExist:
            if request.method == 'POST':
                user = User.objects.get(username=request.user)
                form = UserProfileForm(request.POST)
                if form.is_valid():
                    f = form.save(commit=False)
                    f.user = user
                    f.email = user.email
                    f.aavsocode = 'test'
                    form.save()
                    return redirect('/dashboard/')
            else:
                form = UserProfileForm()
            return render(request, 'register.html', locals())
    else:
        return redirect('/')


def p_view(request):
        return redirect('/')


def p_edit(request):
        return redirect('/')
