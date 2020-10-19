#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Thu 18 June 2020 10:55:12
# Last Modified time: Mon 19 October 2020 22:09:15 

# Description: Managing all forms for Trackers App,
# and what fields will be displayed to the user.

from django import forms
from .models import *


class PainTrackerForm(forms.ModelForm):
    '''PainTrackerForm  defines which fields will be displayed to the user'''

    class Meta:
        model = PainSymptom
        fields = ['date_day', 'time_of_day',
                  'intensity', 'location', 'other_loc']


class SysDigestForm(forms.ModelForm):
    '''SysDigestForm defines which fields will be displayed to the user'''

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
