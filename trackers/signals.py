#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Fri 19 June 2020 01:07:55
# Last Modified time: Tue 23 June 2020 14:33:31 

# Description:

# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import *


# @receiver(post_save, sender=User)
# def create_paintrack(sender, instance, created, **kwargs):
#     if created:
#         PainSymptom.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def create_painloclist(sender, instance, created, **kwargs):
#     if created:
#         PainLocList.objects.create(pain_track=instance)


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()


# pain_track_obj = PainSymptom.objects.create(
#     user=auth.get_user(request),
#     time=time_choices,
#     intensity=intensity_choices)

# for location in locations_block:
#     PainLocList.objects.create(
#         pain_track=pain_track_obj,
#         pain_loc=PainLocation.objects.get_or_create(loc=location))
