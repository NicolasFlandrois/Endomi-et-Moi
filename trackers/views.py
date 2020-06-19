#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 16 June 2020 14:23:42
# Last Modified time: Fri 19 June 2020 02:15:38 

# Description:

from django.contrib import auth
# from django.http import HttpResponseRedirect
# from django.views.generic import ListView, DetailView
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


@login_required
def pain_tracker(request):
    if request.method == 'POST':
        form = PainTrackerForm(request.POST)

        try:
            # if form.is_valid():
            # form.save()
            messages.success(
                request, 'Votre suivi Douleur a bien été enregistré')

            # else:
            #     raise

        except Exception as e:
            print(e)
            messages.warning(
                request, 'Erreur d\'enregistrement')

        return redirect('home')

    elif request.method == 'GET':
        pass

    form = PainTrackerForm()
    title = 'Enregistrer une Douleur'
    return render(request, 'trackers/tracker.html', {'form': form, 'title': title})
