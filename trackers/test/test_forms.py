#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 02 June 2020 15:28:13
# Last Modified time: Mon 19 October 2020 22:20:42 

# Description:
from django.test import TransactionTestCase
from trackers.forms import PainTrackerForm, SysDigestForm
from django.contrib.auth.models import User
from datetime import datetime


class TestForms(TransactionTestCase):
    """Class Testing Forms in Trackers App"""

    def test_PainTrackerForm(self):
        """Testing PainTrackerForm Class"""

        self.user_1 = User.objects.create_user(
            username='testuser', password='12345',
            email='boggusmail@boggusmail.net'
        )

        form = PainTrackerForm(data={
            'date_added': datetime(2020, 9, 10),
            'user': self.user_1,
            'date_day': datetime(2020, 9, 8),
            'time_of_day': 'Matin',
            'intensity': 10,
            'location': 'Plexus',
            'other_loc': 'Here'
        })
        self.assertFalse(form.is_valid())

    def test_SysDigestForm(self):
        """Testing SysDigestForm Class"""
        self.user_1 = User.objects.create_user(
            username='testuser', password='12345',
            email='boggusmail@boggusmail.net'
        )

        form = SysDigestForm(data={
            'date_added': datetime(2020, 9, 10),
            'user': self.user_1,
            'food': 'Fruits',
            'meal': 'Repas léger',
            'nb_meal': 'Plus de 3 Repas',
            'digest': 'Gas',
            'transit': 'Normale',
            'other_food': 'Test_66',
            'other_digest': 'Test_99',
            'other_transit': 'Test_BB8'
        })

        self.assertFalse(form.is_valid())
