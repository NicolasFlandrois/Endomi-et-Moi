#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 02 June 2020 15:28:13
# Last Modified time: Mon 19 October 2020 22:31:23 

# Description:
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Profile


class TestViews(TestCase):
    """Class Testing Views in Charts App"""

    def setUp(self):
        """Set Up variables used in this test"""
        self.client = Client()
        self.chart_url = reverse('graph')

        self.user_1 = User.objects.create_user(
            username='testuser', password='12345',
            email='boggusmail@boggusmail.net'
        )

    # Testing Function based views
    def test_charts_GET(self):
        """Testing the charts GET method's function"""
        logged_in = self.client.login(username='testuser', password='12345')
        response = self.client.get(self.chart_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'charts/chart.html')
