#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 16 June 2020 14:23:42
# Last Modified time: Thu 18 June 2020 23:13:37

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


@login_required
def pain_tracker(request):
    if request.method == 'POST':
        form = PainTrackerForm(request.POST)
        if form.is_valid():

            time_choices = form.cleaned_data.get('time_choices', '')
            intensity_choices = form.cleaned_data.get('intensity_choices', '')
            locations_choices = form.cleaned_data.get('location_choices', [])
            other_locations = form.cleaned_data.get('location_choices', [])

            locations_block = [capitalize(n) for n in set(
                locations_choices + other_locations)]

            PainSymptom.save(
                user=auth.get_user(request),
                time=time_choices,
                intensity=intensity_choices,
                locations=locations_block)

        messages.success(request, 'Votre suivi Douleur a bien été enregistré')
        return redirect('home')

    elif request.method == 'GET':
        pass

    form = PainTrackerForm()
    title = 'Enregistrer une Douleur'
    return render(request, 'trackers/pain_tracker.html', {'form': form, 'title': title})
