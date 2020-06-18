#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Thu 18 June 2020 10:55:12
# Last Modified time: Thu 18 June 2020 17:33:18

# Description:
from django import forms
from .models import PainSymptom

class PainTrackerForm(forms.Form):

    time_choices = forms.MultipleChoiceField(choices=[],
                                             label='Quand ?',
                                             required=False,
                                             widget=forms.SelectDateWidget(
        attrs={
            'class': 'form-control',
        }
    ))

    intensity_choices = forms.MultipleChoiceField(choices=[n[1] for n in PainSymptom.INTENSITY_CHOICE],
                                                  label='Intensité ?',
                                                  required=True,
                                                  widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ))

    location_choices = forms.MultipleChoiceField(choices=[n[1] for n in PainSymptom.LOC_CHOICE],
                                                 label='Localisation ?',
                                                 required=True,
                                                 widget=forms.CheckboxSelectMultiple(
        attrs={
            'class': 'form-control'
        }
    ))

    other_location = forms.CharField(label='Other', max_length=100, required=False,
                                     widget=forms.TextInput(
                                         attrs={
                                             'class': 'form-control',
                                             'placeholder': 'Autre Localisation de la Douleur ?'
                                         }
                                     ))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        init_loc = ['Lombaire', 'Abdominale', 'Intra-utérine',
                    'Intestinale', 'Digestive', 'Plexus', 'Aucune']
        data_locations = [loc for loc in PainSymptom.objects.order_by(
            'location').values_list('location', flat=True).distinct()]
        unique_locations = set(init_loc + data_locations)

        self.fields['intensity_choices'].choices = [(n, n) for n in range(11)]
        self.fields['location_choices'].choices = [
            (loc, loc) for loc in unique_locations]

   # class Meta:
    #     model = PainSymptom
    #     fields = ['time', 'intensity', 'location']
