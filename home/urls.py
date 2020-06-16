#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 02 June 2020 15:29:27
# Last Modified time: Tue 16 June 2020 14:37:22 

# Description:
from django.urls import path
from . import views

urlpatterns = [
    path('legal/', views.legal, name='legal'),
    path('', views.home, name='home'),
]
