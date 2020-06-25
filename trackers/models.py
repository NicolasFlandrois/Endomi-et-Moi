#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 16 June 2020 14:23:30
# Last Modified time: Thu 25 June 2020 12:43:00 

# Description:

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date


class Constants(models.Model):
    """
    PainLocation is a single répertoire of all pain locations.
        Loc defines the Location's name.
        Show defines if we show this option to the public users.
    """
    id = models.AutoField(primary_key=True)
    cat = models.CharField(max_length=10, null=False, default='Unknown')
    name = models.CharField(max_length=20)
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
        # Constants for Pain Locations for PainSymptom class
        loc_lombaire = Constants.objects.get_or_create(
            cat='loc', name='lombaire', show=True)
        loc_abdominale = Constants.objects.get_or_create(
            cat='loc', name='abdominale', show=True)
        loc_intra_uterine = Constants.objects.get_or_create(
            cat='loc', name='intra-utérine', show=True)
        loc_intestinale = Constants.objects.get_or_create(
            cat='loc', name='intestinale', show=True)
        loc_digestive = Constants.objects.get_or_create(
            cat='loc', name='digestive', show=True)
        loc_plexus = Constants.objects.get_or_create(
            cat='loc', name='plexus', show=True)
        loc_aucun = Constants.objects.get_or_create(
            cat='loc', name='_aucun', show=True)
        loc_autres = Constants.objects.get_or_create(
            cat='loc', name='_autres', show=True)
        # Constants for Food for SysDigest class
        food_sucre = Constants.objects.get_or_create(
            cat='food', name='sucre', show=True)
        food_caféine = Constants.objects.get_or_create(
            cat='food', name='caféine', show=True)
        food_théine = Constants.objects.get_or_create(
            cat='food', name='théine', show=True)
        food_gluten = Constants.objects.get_or_create(
            cat='food', name='gluten', show=True)
        food_fruits = Constants.objects.get_or_create(
            cat='food', name='fruits', show=True)
        food_légumes = Constants.objects.get_or_create(
            cat='food', name='légumes', show=True)
        food_céréales = Constants.objects.get_or_create(
            cat='food', name='céréales', show=True)
        food_légumineuse = Constants.objects.get_or_create(
            cat='food', name='légumineuse', show=True)
        food_lactose = Constants.objects.get_or_create(
            cat='food', name='lactose', show=True)
        food_lait_veg = Constants.objects.get_or_create(
            cat='food', name='lait végétal', show=True)
        food_viande_rouge = Constants.objects.get_or_create(
            cat='food', name='viande rouge', show=True)
        food_viande_blanche = Constants.objects.get_or_create(
            cat='food', name='viande blanche', show=True)
        food_poisson = Constants.objects.get_or_create(
            cat='food', name='poisson', show=True)
        food_epicé = Constants.objects.get_or_create(
            cat='food', name='epicé', show=True)
        food_gras = Constants.objects.get_or_create(
            cat='food', name='gras', show=True)
        food_aucun = Constants.objects.get_or_create(
            cat='food', name='_aucun', show=True)
        food_autres = Constants.objects.get_or_create(
            cat='food', name='_autres', show=True)
        # Constants for Digestion for SysDigest class
        digest_normal = Constants.objects.get_or_create(
            cat='digest', name='normal', show=True)
        digest_crampes = Constants.objects.get_or_create(
            cat='digest', name='crampes', show=True)
        digest_gaz = Constants.objects.get_or_create(
            cat='digest', name='gaz', show=True)
        digest_faim = Constants.objects.get_or_create(
            cat='digest', name='sensation de faim', show=True)
        digest_aucun = Constants.objects.get_or_create(
            cat='digest', name='_aucun', show=True)
        digest_autres = Constants.objects.get_or_create(
            cat='digest', name='_autres', show=True)
        # Constants for Transit for SysDigest class
        transit_normal = Constants.objects.get_or_create(
            cat='transit', name='normal', show=True)
        transit_diarrhée = Constants.objects.get_or_create(
            cat='transit', name='diarrhée', show=True)
        transit_constipation = Constants.objects.get_or_create(
            cat='transit', name='constipation', show=True)
        transit_hémorroïdes = Constants.objects.get_or_create(
            cat='transit', name='hémorroïdes', show=True)
        transit_aucun = Constants.objects.get_or_create(
            cat='transit', name='_aucun', show=True)
        transit_autres = Constants.objects.get_or_create(
            cat='transit', name='_autres', show=True)


class PainSymptom(models.Model):
    """
    PainSymptom is the data model to track down pain symptoms.
    When did the pain occure, Where on the body, and how intense?
    2 specific fields allow the user to track the data after the event,
    by specifying the date (in date_day),
    and the time/period during that day (in time_of_day)
    """
    locs = Constants.objects.all().filter(
        cat='loc', show=True).order_by('-name')
    # locs = []  # Activate this variable when applying new migrations
    # Fetch all choices option from Constants, only those show=True

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
                                    (location.name.title(), location.name.title()) for location in locs]
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
            if Constants.objects.filter(name=location).exists() == False:
                new_loc = Constants(cat='loc', name=location,
                                    show=False)
                new_loc.save()


class SysDigest(models.Model):
    """
    SysDigest is the data model to track down Food Habits.
    """
    foods = Constants.objects.all().filter(
        cat='food', show=True).order_by('-name')
    digests = Constants.objects.all().filter(
        cat='digest', show=True).order_by('-name')
    transits = Constants.objects.all().filter(
        cat='transit', show=True).order_by('-name')
    # foods = []  # Activate this variable when applying new migrations
    # digests = []  # Activate this variable when applying new migrations
    # transits = []  # Activate this variable when applying new migrations
    # Fetch all choices option from Constants, only those show=True

    id = models.AutoField(primary_key=True)
    date_added = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.CharField('Quel type de nourriture ?',
                            default='Null',
                            max_length=50,
                            null=True,
                            choices=[
                                    (food.name.title(), food.name.title()) for food in foods]
                            )

    meal = models.CharField('Quel type de repas ?',
                            default='Aucun',
                            max_length=20,
                            null=True,
                            choices=[('Repas léger', 'Repas léger'),
                                     ('Repas lourd', 'Repas lourd'),
                                     ('Aucun', 'Aucun')])

    nb_meal = models.CharField('Combien de repas ?',
                               max_length=30,
                               null=True,
                               choices=[('3 Repas', '3 Repas'),
                                        ('2 Repas', '2 Repas'),
                                        ('1 Repas', '1 Repas'),
                                        ('Plus de 3 Repas', 'Plus de 3 Repas'),
                                        ('Jeûne 24h', 'Jeûne 24h'),
                                        ('Jeûne long (plusieurs jours)', 'Jeûne long (plusieurs jours)')])

    digest = models.CharField('Quel type de digestion ?',
                              default='Null',
                              max_length=50,
                              null=False,
                              choices=[
                                  (digest.name.title(), digest.name.title()) for digest in digests]
                              )

    transit = models.CharField('Quel type de transit intestinale ?',
                               default='Null',
                               max_length=50,
                               null=False,
                               choices=[
                                   (transit.name.title(), transit.name.title()) for transit in transits]
                               )

    other_food = models.CharField('Avez-vous mangé d\'autres catégories d\'aliments ?',
                                  max_length=20,
                                  default='_Aucun',
                                  null=False,
                                  help_text="Si plusieurs nouveaux aliments, séparez avec une <em>virgule</em)."
                                  )

    other_digest = models.CharField('Avez-vous des symptômes digestifs autres ?',
                                    max_length=20,
                                    default='_Aucun',
                                    null=False,
                                    help_text="Si plusieurs nouveaux symdrômes digestifs, séparez avec une <em>virgule</em)."
                                    )

    other_transit = models.CharField('Avez-vous des symptômes de transit autres ?',
                                     max_length=20,
                                     default='_Aucun',
                                     null=False,
                                     help_text="Si plusieurs nouveaux syndrômes de transit, séparez avec une <em>virgule</em)."
                                     )

    def __str__(self):
        """__str__ display when calling the object in consol"""
        return f"User: {self.user.username}, \
Food: {self.food}, \
Digest: {self.digest}, \
Transit: {self.transit}, \
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

        foods = self.other_food.split(',')
        for food in foods:
            food = food.strip().lower()
            if Constants.objects.filter(name=food).exists() == False:
                new_food = Constants(cat='food', name=food,
                                     show=False)
                new_food.save()

        digests = self.other_digest.split(',')
        for digest in digests:
            digest = digest.strip().lower()
            if Constants.objects.filter(name=digest).exists() == False:
                new_digest = Constants(cat='digest', name=digest,
                                       show=False)
                new_digest.save()

        transits = self.other_transit.split(',')
        for transit in transits:
            transit = transit.strip().lower()
            if Constants.objects.filter(name=transit).exists() == False:
                new_transit = Constants(cat='transit', name=transit,
                                        show=False)
                new_transit.save()
