#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 16 June 2020 14:23:42
# Last Modified time: Wed 24 June 2020 15:02:07

# Description:

from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date
from .models import *
from .forms import *


@login_required
def pain_tracker(request):
    print('pouloulou 1')
    if request.method == 'POST':
        print('pouloulou 2 - Post')
        form = PainTrackerForm(request.POST)
        print('pouloulou 3', [
              n if '_post' in n else None for n in request.__dict__.items()])

        if form.is_valid():  # Issue is here... data doesn't pass through form validation

            print('pouloulou 4 - valid form')
            # p_new = PainSymptom(instance=request.user)
            # p_new.user = auth.get_user(request)
            # tmp_date_day = form.cleaned_data['date_day']
            # p_new.date_day = tmp_date_day if tmp_date_day is True else date.today()
            # p_new.time_of_day = form.cleaned_data['time_of_day']
            # p_new.intensity = form.cleaned_data['intensity']
            # p_new.location = form.cleaned_data['location']
            # p_new.other_loc = form.cleaned_data['other_loc']

            # print('pouloulou 5', p_new)

            # p_new.save(other_loc=p_new.other_loc)

            print('pouloulou 6')
            form.save(commit=True)

            messages.success(
                request, 'Votre suivi Douleur a bien été enregistré')

            print('pouloulou 7 - Success')

        else:
            print('pouloulou 8 - Failed')
            messages.warning(
                request, 'Votre requête n\'a pas été enregistré')

        return redirect('home')

    else:
        print('pouloulou 9 - Get')
        form = PainTrackerForm()

    print('pouloulou 10')

    context = {
        'form': form,
        'title': 'Enregistrer une Douleur'
    }

    print('pouloulou 11')

    return render(request, 'trackers/tracker.html', context)
