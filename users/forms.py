#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 02 June 2020 23:51:13
# Last Modified time: Thu 18 June 2020 10:54:49 

# Description:
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

class ProfileRegisterForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['accord_de_don_des_données_à_la_recherche_médicale']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image', 'accord_de_don_des_données_à_la_recherche_médicale']
