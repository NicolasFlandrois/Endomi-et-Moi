#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Thu 18 June 2020 10:55:12
# Last Modified time: Fri 19 June 2020 02:15:11 

# Description:
from django.contrib import auth
from django import forms
from .models import *

class PainTrackerForm(forms.Form):

    time_choices = forms.MultipleChoiceField(choices=[],
                                             label='Quand est-elle apparue ?',
                                             required=False,
                                             widget=forms.SelectDateWidget(
        attrs={
            'class': 'form-control',
        }
    ))

    intensity_choices = forms.MultipleChoiceField(choices=[],
                                                  label='Quel est son Intensité ?',
                                                  required=True,
                                                  widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))

    locations_choices = forms.MultipleChoiceField(choices=[],
                                                  label='Quel est la Localisation de la douleur?',
                                                  required=True,
                                                  widget=forms.CheckboxSelectMultiple(
        attrs={
            'class': 'form-control'
        }
    ))

    other_locations = forms.CharField(label='Other', max_length=100, required=False,
                                      widget=forms.TextInput(
                                          attrs={
                                              'class': 'form-control',
                                              'placeholder': 'Autre Localisation de la Douleur ?'
                                          }
                                      ))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_loc = ['Lombaire', 'Abdominale', 'Intra-utérine',
                         'Intestinale', 'Digestive', 'Plexus', 'Aucune']
        self.data_locations = [loc for loc in PainLocation.objects.order_by(
            'loc').values_list('loc', flat=True).distinct()]
        self.unique_locations = sorted(
            set(self.init_loc + self.data_locations))

        self.fields['intensity_choices'].choices = [
            (n, n) for n in range(11)]
        self.fields['locations_choices'].choices = [
            (loc, loc) for loc in self.unique_locations]

    # def save(self):

    #     loc_chosen = []
    #     for attr, value in self.fields['locations_choices'].__dict__.items():
    #         print(value)
    #         loc_chosen.append(value)

    #     for attr, value in self.fields['other_locations'].__dict__.items():
    #         print(value)
    #         loc_chosen.append(value)

    #     locations_block = list(set(loc_chosen))

    #     print(locations_block)

    #     pain_track_obj = PainSymptom.objects.create(
    #         user=auth.get_user(request),
    #         time=self.fields['time_choices'].get(),
    #         intensity=self.fields['intensity_choices'].get())

    #     for location in locations_block:
    #         PainLocList.objects.create(
    #             pain_track=pain_track_obj,
    #             pain_loc=PainLocation.objects.get_or_create(loc=location))

# How to fetch the information from the form, and save data in DB?
