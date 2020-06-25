#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 16 June 2020 14:23:42
# Last Modified time: Thu 25 June 2020 14:20:50

# Description:

from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import *
from .forms import *


@login_required
def pain_tracker(request):
    if request.method == 'POST':
        try:
            instance = PainSymptom()
            instance.user = auth.get_user(request)
            tmp_date_day = request.POST.get('date_day')
            instance.date_day = datetime.strptime(tmp_date_day, "%d/%m/%Y")
            instance.time_of_day = request.POST.get('time_of_day')
            instance.intensity = request.POST.get('intensity')
            instance.location = request.POST.get('location')
            instance.other_loc = request.POST.get('other_loc').lower()
            instance.save()
            messages.success(request, 'Vos réponses ont bien été enregistrés')
            return redirect('home')
        except Exception as e:
            print(e)
            messages.warning(request, 'Vos réponses n\'ont pas été enregstrés')
            return redirect('douleurs')
    else:
        form = PainTrackerForm()
    context = {
        'form': form,
        'title': 'Enregistrer une Douleur'
    }
    return render(request, 'trackers/tracker.html', context)


@login_required
def digest_tracker(request):
    if request.method == 'POST':
        try:
            instance = SysDigest()
            instance.user = auth.get_user(request)

            req = dict(request.POST)

            instance.food = ', '.join(req['food'])
            instance.meal = request.POST.get('meal')
            instance.nb_meal = request.POST.get('nb_meal')
            instance.digest = request.POST.get('digest')
            instance.transit = request.POST.get('transit')
            instance.other_food = request.POST.get('other_food').lower()
            instance.other_digest = request.POST.get('other_digest').lower()
            instance.other_transit = request.POST.get('other_transit').lower()

            instance.save()
            messages.success(request, 'Vos réponses ont bien été enregistrés')
            return redirect('home')
        except Exception as e:
            print(e)
            messages.warning(request, 'Vos réponses n\'ont pas été enregstrés')
            return redirect('digestif')
    else:
        form = SysDigestForm()
    context = {
        'form': form,
        'title': 'Enregistrer un Suivi de Repas'
    }
    return render(request, 'trackers/tracker.html', context)
