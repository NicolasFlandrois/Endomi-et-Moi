#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 02 June 2020 15:29:28
# Last Modified time: Tue 16 June 2020 14:37:21 

# Description:
from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html', {'title': 'Accueil'})


def legal(request):
    return render(request, 'home/legal.html', {'title': 'Mentions Legales'})
