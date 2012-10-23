# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.conf.urls.defaults import *
from django.contrib.auth import authenticate, login
from django.conf import settings


def home(request):
    return render_to_response('base.html', locals())
