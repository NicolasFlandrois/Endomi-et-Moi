#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 02 June 2020 15:28:20
# Last Modified time: Tue 16 June 2020 22:34:55 

# Description:
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # u_form = UserRegisterForm(request.POST)
        # p_form = ProfileRegisterForm(request.POST,
        #                              instance=request.user.profile)
        # if u_form.is_valid() and p_form.is_valid():
        if form.is_valid():
            form.save()
            # u_form.save()
            # p_form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request,
                f'Compte créé pour {username}! Vous pouvez maintenant vous connecter.')
            return redirect('login')
    else:
        form = UserRegisterForm()
        # u_form = UserRegisterForm()
        # p_form = ProfileRegisterForm()

    context = {
        'form': form,
        # 'u_form': u_form,
        # 'p_form': p_form,
        'title': 'Créer un compte'
    }

    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Votre profil a été mis à jour!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': 'Mon Profil'
    }

    return render(request, 'users/profile.html', context)
