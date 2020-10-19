#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 02 June 2020 15:28:13
# Last Modified time: Mon 19 October 2020 22:27:01 

# Description:
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from trackers.models import Constants, PainSymptom, SysDigest
from datetime import datetime


class TestViews(TestCase):
    """Class Testing Views in Trackers App"""

    def setUp(self):
        """Set Up variables used in this test"""
        self.client = Client()
        self.pain_url = reverse('douleurs')
        self.digest_url = reverse('digestif')

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
            other_loc='None')

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

    # Testing Function based views

    def test_pain_GET(self):
        """Testing the pain GET method's function"""
        logged_in = self.client.login(username='testuser', password='12345')
        response = self.client.get(self.pain_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'trackers/tracker.html')

    def test_digest_GET(self):
        """Testing the digest GET method's function"""
        logged_in = self.client.login(username='testuser', password='12345')
        response = self.client.get(self.digest_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'trackers/tracker.html')
