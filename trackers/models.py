#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 16 June 2020 14:23:30
# Last Modified time: Wed 24 June 2020 23:26:31 

# Description:

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date


class PainLocConstants(models.Model):
    """
    PainLocation is a single répertoire of all pain locations.
        Loc defines the Location's name.
        Show defines if we show this option to the public users.
    """
    id = models.AutoField(primary_key=True)
    loc = models.CharField(max_length=20)
    show = models.BooleanField(null=False, default=False)

    def __str__(self):
        """__str__ display when calling the object in consol"""
        return f"Pain Location choices: {self.loc} | Show to users: {self.show}"

    def init_populate(self, *args, **kwargs):
        '''
        This functionn called in shell,
        with `python manage.py shell` command,
        will allow to populate constants table, for the initial setup
        '''
        lombaire = PainLocConstants(loc='lombaire', show=True)
        abdominale = PainLocConstants(loc='abdominale', show=True)
        intra_uterine = PainLocConstants(loc='intra-utérine', show=True)
        intestinale = PainLocConstants(loc='intestinale', show=True)
        digestive = PainLocConstants(loc='digestive', show=True)
        plexus = PainLocConstants(loc='plexus', show=True)
        aucune = PainLocConstants(loc='_aucun', show=True)
        autres = PainLocConstants(loc='_autres', show=True)
        lombaire.save()
        abdominale.save()
        intra_uterine.save()
        intestinale.save()
        digestive.save()
        plexus.save()
        aucune.save()
        autres.save()


class PainSymptom(models.Model):
    """
    PainSymptom is the data model to track down pain symptoms.
    When did the pain occure, Where on the body, and how intense?
    2 specific fields allow the user to track the data after the event,
    by specifying the date (in date_day),
    and the time/period during that day (in time_of_day)
    """
    locs = PainLocConstants.objects.all().filter(show=True).order_by('-loc')
    # Fetch all choices option from PainLocConstants, only those show=True

    id = models.AutoField(primary_key=True)
    date_added = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_day = models.DateField(
        'Quand est apparue la douleur ?',
        default=date.today, null=False,
        help_text="Veuillez rentrer la date au format: <em>JJ/MM/AAAA</em>.")
    time_of_day = models.CharField('Quel temps dans la journée ?',
                                   default='Null',
                                   max_length=10,
                                   null=False)
    intensity = models.CharField('Quel est sont intensité ?',
                                 max_length=2,
                                 default=0,
                                 null=False,
                                 choices=[(n, n) for n in range(11)])
    location = models.CharField('Quel est la Localisation de la douleur?',
                                max_length=20,
                                default='_Aucune',
                                null=False,
                                choices=[
                                    (location.loc.title(), location.loc.title()) for location in locs]
                                )
    other_loc = models.CharField('La douleur est-elle à un autre endroit?',
                                 max_length=20,
                                 default='_Aucun',
                                 null=False,
                                 help_text="Si plusieurs nouvelles localisations, séparez avec une <em>virgule</em)."
                                 )

    def __str__(self):
        """__str__ display when calling the object in consol"""
        return f"User: {self.user.username}, \
Location: {self.location}, \
Intensity: {self.intensity}, \
Date: {self.date_added}"

    def save(self, *args, **kwargs):
        """
        save()
        This function saves the instance object to the database.
        Here I modified it, so if new locations are detected
        from 'Other Locations', it could save those new location in our
        constants location table.
        """
        super().save(*args, **kwargs)
        locations = self.other_loc.split(',')
        for location in locations:
            location = location.strip().lower()
            if PainLocConstants.objects.filter(loc=location).exists():
                pass
            else:
                new_loc = PainLocConstants(loc=location,
                                           show=False)
                new_loc.save()
