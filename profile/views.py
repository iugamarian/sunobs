# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from sunoss.panel.models import Profile


def panel(request):
    if request.user.is_authenticated():
        me = Profile.objects.get(user=request.user)
        return render_to_response('panel.html', locals())
    else:
        return redirect('/')
