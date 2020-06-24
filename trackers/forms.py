#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Thu 18 June 2020 10:55:12
# Last Modified time: Wed 24 June 2020 23:00:29 

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
                                            widget=forms.RadioSelect(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = PainSymptom
        fields = ['date_day', 'time_of_day',
                  'intensity', 'location', 'other_loc']
