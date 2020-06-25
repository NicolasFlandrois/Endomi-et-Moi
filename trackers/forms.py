#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Thu 18 June 2020 10:55:12
# Last Modified time: Thu 25 June 2020 14:29:36

# Description:
from django.contrib import auth
from django import forms
from .models import *

TIME_SET = [
    'Matin',
    'Midi',
    'Après-Midi',
    'Soir',
    'Nuit'
]


class PainTrackerForm(forms.ModelForm):
    '''PainTrackerForm Docstring'''

    time_of_day = forms.MultipleChoiceField(choices=[(n, n) for n in TIME_SET],
                                            label='A quel moment dans la journée ?',
                                            required=True,
                                            widget=forms.CheckboxSelectMultiple(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = PainSymptom
        fields = ['date_day', 'time_of_day',
                  'intensity', 'location', 'other_loc']


class SysDigestForm(forms.ModelForm):
    '''PainTrackerForm Docstring'''

    foods = Constants.objects.all().filter(
        cat='food', show=True).order_by('-name')

    food = forms.ChoiceField(choices=[
        (food.name.title(), food.name.title()) for food in foods],
        required=False,
        widget=forms.CheckboxSelectMultiple(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = SysDigest
        fields = ['food',
                  'meal',
                  'nb_meal',
                  'digest',
                  'transit',
                  'other_food',
                  'other_digest',
                  'other_transit']
