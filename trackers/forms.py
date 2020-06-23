#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Thu 18 June 2020 10:55:12
# Last Modified time: Tue 23 June 2020 23:07:00

# Description:
from django.contrib import auth
from django import forms
from .models import *

TIME_SET = [
    'Matin',
    'Midi',
    'Après-Midi',
    'Soire',
    'Nuit'
]


class PainTrackerForm(forms.ModelForm):
    date_day = forms.MultipleChoiceField(choices=[],
                                         label='Quand est-elle apparue ?',
                                         required=False,
                                         widget=forms.SelectDateWidget(
        attrs={
            'class': 'form-control',
        }
    ))

    time_of_day = forms.MultipleChoiceField(choices=[(n, n) for n in TIME_SET],
                                            label='A quel moment dans la journée ?',
                                            required=True,
                                            widget=forms.CheckboxSelectMultiple(
        attrs={
            'class': 'form-control',
        }
    ))

    other_loc = forms.CharField(label='La douleur est-elle à un autre endroit?',
                                max_length=100,
                                required=False,
                                widget=forms.TextInput(
                                    attrs={
                                        'class': 'form-control',
                                    }
                                ))

    class Meta:
        model = PainSymptom
        fields = ['date_day', 'time_of_day',
                  'intensity', 'location', 'other_loc']
