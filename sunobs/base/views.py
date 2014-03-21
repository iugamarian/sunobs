# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.decorators import login_required

from sunobs.base.forms import UserForm

User = get_user_model()


def index(request):
    return render(request, 'home.html', locals())


@login_required
def p_edit(request):
    if request.method == 'POST':
        me = User.objects.get(email=request.user)
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.email = me.email
            f.aavsocode = 'test'
            form.save()
            return redirect('/dashboard/')
    else:
        form = UserForm()
    return render(request, 'o_edit.html', {'me': me, 'form': form})


def p_view(request):
    return redirect('/dashboard/')


def logout_user(request):
    logout(request)
    return redirect('/')