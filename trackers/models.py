#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 16 June 2020 14:23:30
# Last Modified time: Thu 18 June 2020 23:05:26 

# Description:

from django.db import models, transaction
from django.utils import timezone
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


class PainLocation(models.Model):
    """PainLocation is a single répertoire of all pain locations"""
    loc = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        with transaction.atomic():
            for loc in location:
                if len(loc) == 0:
                    continue

                if Vote.objects.filter(loc=loc).exists():
                    pass
                else:
                    Vote.objects.create(loc=loc, count=1)


class PainSymptom(models.Model):
    """docstring for PainSymptom"""

    date_added = models.DateTimeField(default=timezone.now)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    intensity = models.CharField(max_length=2,
                                 default=0, null=True)
    location = models.ForeignKey(
        PainLocation, max_length=20, null=True, on_delete=models.CASCADE)

    def __str__(self):
        """__str__ display when calling the object in consol"""
        return f"User: {self.user.username}, Intensity: {self.product}, \
Where: {self.location} Date: {self.date_added}"

    def save(self, *args, **kwargs):
        """Saving Forms answers/choices into database"""
        super().save(*args, **kwargs)
        PainLocation.save(locations)

        temp_loc_new = PainLocation()
        loc_dict_new = {value: key for key,
                        value in temp_loc_new.__dict__.items()}

        loc_id_list = [loc_dict_new[loc] for loc in location]

        PainSymptom.objetcts.create(
            user=user, time=time, intensity=intensity, location=loc_id_list)
