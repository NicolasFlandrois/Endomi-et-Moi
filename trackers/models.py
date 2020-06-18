#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 16 June 2020 14:23:30
# Last Modified time: Thu 18 June 2020 17:00:13

# Description:
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


class PainSymptom(models.Model):
    """docstring for PainSymptom"""
    INTENSITY_CHOICE = ((n, n) for n in range(11))
    LOC_CHOICE = (
        ('Lombaire', 'Lombaire'),
        ('Abdominale', 'Abdominale'),
        ('Intra-utérine', 'Intra-utérine'),
        ('Intestinale', 'Intestinale'),
        ('Digestive', 'Digestive'),
        ('Plexus', 'Plexus'),
        ('Aucune', 'Aucune'),
        ('Autres', 'Autres')
    )
    # WHEN = (
    #     ('Maintenant', 'Maintenant'),
    #     ('Hier', 'Hier'),
    #     ('Hier Soir', 'Hier Soir'),
    #     ('La Nuit Dernière', 'La Nuit Dernière'),
    #     ('Ce Matin', 'Ce Matin'),
    #     ('Ce Midi', 'Ce Midi'),
    #     ('Cet Après-midi', 'Cet Après-midi'),
    #     ('Début de Soirée', 'Début de Soirée'),
    #     ('Ce Soir', 'Ce Soir'),
    #     ('Cette Nuit', 'Cette Nuit')
    # )

    date_added = models.DateTimeField(default=timezone.now)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    intensity = models.CharField(max_length=2,
                                 choices=INTENSITY_CHOICE,
                                 default=0, null=True)
    location = models.CharField(max_length=20,
                                choices=LOC_CHOICE,
                                default='Aucune', null=True)
    other_location = models.CharField(max_length=20,
                                      default='Aucune', null=True)

    def __str__(self):
        """__str__ display when calling the object in consol"""
        return f"User: {self.user.username}, Intesity: {self.product}, \
Where: {self.location} Date: {self.date_added}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
