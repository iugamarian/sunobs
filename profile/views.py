# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from sunoss.profile.models import UserProfile


def profile(request):
    if request.user.is_authenticated():
        #me = UserProfile.objects.get(user=request.user)
        return render_to_response('profile.html', locals())
    else:
        return redirect('/')
