# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.template import Context, RequestContext, loader

from django.conf.urls.defaults import *
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'home.html', locals())


def logout_user(request):
    logout(request)
    return redirect('/')
