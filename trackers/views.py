#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 16 June 2020 14:23:42
# Last Modified time: Wed 24 June 2020 23:00:49 

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
