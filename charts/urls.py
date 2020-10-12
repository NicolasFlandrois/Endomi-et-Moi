#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 02 June 2020 15:29:27
# Last Modified time: Wed 07 October 2020 17:45:38 

# Description: Charts URL dispatch
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.ChartView.as_view(), name='graph'),
    url(r'^api/chart/data/$', views.ChartData.as_view()),
]
