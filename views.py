# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.template import Context, RequestContext, loader

from django.conf.urls.defaults import *
from django.contrib.auth import authenticate, login, logout

def home(request):
    if request.user.is_authenticated():
        return redirect('/me/')
    return render(request, 'base.html', locals())


def logout_user(request):
    logout(request)
    return redirect('/')
