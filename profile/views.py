# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from sunoss.profile.models import UserProfile, UserProfileForm


def me(request):
    if request.user.is_authenticated():
        email = request.user.email
        try:
            me = get_object_or_404(UserProfile.objects.get(user=request.user))
        except UserProfile.DoesNotExist:
            return redirect('/register/')
        return render_to_response('me.html', locals())
    else:
        return redirect('/')


def register(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = UserProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/me/')
        else:
            form = UserProfileForm()
        return render_to_response('register.html', locals())
    else:
        return redirect('/')
