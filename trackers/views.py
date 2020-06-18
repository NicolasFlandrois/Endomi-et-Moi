#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 16 June 2020 14:23:42
# Last Modified time: Thu 18 June 2020 16:50:27 

# Description:

from django.contrib import auth
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import PainSymptom
from .forms import PainTrackerForm


# @login_required
# def pain_tracker(request):
#     if request.method == 'POST':
#         form = PainTrackerForm(
#             request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(
#                 request, 'Votre suivi Douleur a bien été enregistré')
#             return redirect('home')

#     else:
#         form = PainTrackerForm(
#             request.POST)

#     context = {
#         'form': form,
#         'title': 'Suivi: Douleurs'
#     }

#     return render(request, 'trackers/pain_tracker.html', context)


# class PainTrackerValidView(LoginRequiredMixin, View):
#     model = PainSymptom

#     def get(self, request):

#         form = PainTrackerForm(
#             request.POST, instance=request.user)

#         new_track, created = PainSymptom.objects.get_or_create(
#             user=auth.get_user(request),
#             time=form.time,
#             intensity=form.intensity,
#             location=form.location)

#         if not created:
#             pass

#         # return HttpResponseRedirect('/snacks/favourites')
#         context = {
#             'form': form,
#             'title': 'Suivi: Douleurs'
#         }

#         return render(request, 'trackers/pain_tracker.html', context)


@login_required
def pain_tracker(request):
    if request.method == 'POST':
        form = PainTrackerForm(request.POST)
        if form.is_valid():
            time_choices = form.cleaned_data.get('time_choices', [])
            intensity_choices = form.cleaned_data.get('intensity_choices', '')
            location_choices = form.cleaned_data.get('location_choices', '')

            PainSymptom.object.create(
                user=auth.get_user(request),
                time=time_choices,
                intensity=ensity_choices,
                location=location_choices)
        message = 'Votre suivi Douleur a bien été enregistré'
    elif request.method == 'GET':
        message = ''

    form = PainTrackerForm()
    return render(request, 'trackers/pain_tracker.html', {'form': form, 'message': message})
