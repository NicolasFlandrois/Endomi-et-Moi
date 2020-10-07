#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 02 June 2020 15:29:27
# Last Modified time: Wed 07 October 2020 16:54:12 

# Description:
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chart, name='graph'),
]
