#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 02 June 2020 15:28:13
# Last Modified time: Mon 19 October 2020 10:07:07 

# Description:
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from trackers.models import Constants, PainSymptom, SysDigest
from datetime import datetime


class TestModels(TestCase):
    """Class Testing Models in Trackers App"""

    def setUp(self):
        """Set Up variables used in this test"""

        self.user_1 = User.objects.create_user(
            username='testuser', password='12345',
            email='boggusmail@boggusmail.net'
        )

        self.constant_1 = Constants(
            cat='test', name='Constants_Test_1',
            show=False
        )

        self.pain_1 = PainSymptom(
            date_added=datetime(2020, 9, 10),
            user=self.user_1,
            date_day=datetime(2020, 9, 8),
            time_of_day='Matin',
            intensity=10,
            location='Plexus',
            other_loc=None)

        self.digest_1 = SysDigest(
            date_added=datetime(2020, 9, 10),
            user=self.user_1,
            food='Fruits',
            meal='Repas léger',
            nb_meal='Plus de 3 Repas',
            digest='Gas',
            transit='Normale',
            other_food='Test_66',
            other_digest='Test_99',
            other_transit='Test_BB8')

    def test_Constants(self):
        """Testing the Constants class' object"""
        self.assertEquals(self.constant_1.cat, 'test')
        self.assertEquals(self.constant_1.name, 'Constants_Test_1')
        self.assertEquals(self.constant_1.show, False)

    def test_PainSymptom(self):
        """Testing the PainSymptom class' object"""
        self.assertEquals(self.pain_1.date_added, datetime(2020, 9, 10))
        self.assertEquals(self.pain_1.user.username, 'testuser')
        self.assertEquals(self.pain_1.date_day, datetime(2020, 9, 8))
        self.assertEquals(self.pain_1.time_of_day, 'Matin')
        self.assertEquals(self.pain_1.intensity, 10)
        self.assertEquals(self.pain_1.location, 'Plexus')
        self.assertEquals(self.pain_1.other_loc, None)

    def test_SysDigest(self):
        """Testing the SysDigest class' object"""
        self.assertEquals(self.digest_1.date_added, datetime(2020, 9, 10))
        self.assertEquals(self.digest_1.user.username, 'testuser')
        self.assertEquals(self.digest_1.food, 'Fruits')
        self.assertEquals(self.digest_1.meal, 'Repas léger')
        self.assertEquals(self.digest_1.nb_meal, 'Plus de 3 Repas')
        self.assertEquals(self.digest_1.digest, 'Gas')
        self.assertEquals(self.digest_1.transit, 'Normale')
        self.assertEquals(self.digest_1.other_food, 'Test_66')
        self.assertEquals(self.digest_1.other_digest, 'Test_99')
        self.assertEquals(self.digest_1.other_transit, 'Test_BB8')
