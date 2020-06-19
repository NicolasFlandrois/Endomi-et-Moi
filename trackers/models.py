#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 16 June 2020 14:23:30
# Last Modified time: Fri 19 June 2020 00:19:52 

# Description:

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


class PainLocation(models.Model):
    """PainLocation is a single répertoire of all pain locations"""
    loc = models.CharField(max_length=20)


class PainSymptom(models.Model):
    """docstring for PainSymptom"""

    date_added = models.DateTimeField(default=timezone.now)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    intensity = models.CharField(max_length=2,
                                 default=0, null=True)

    def __str__(self):
        """__str__ display when calling the object in consol"""
        return f"User: {self.user.username}, Intensity: {self.intensity}, \
Date: {self.date_added}"


class PainLocList(models.Model):
    pain_track = models.ForeignKey(PainSymptom, on_delete=models.CASCADE)
    pain_loc = models.ForeignKey(PainLocation, on_delete=models.CASCADE)

    def __str__(self):
        """__str__ display when calling the object in consol"""
        return f"User : {self.pain_track.user.username} \
Pain Tracker n°: {self.pain_track}, Pain Location : {self.pain_loc.loc}"
