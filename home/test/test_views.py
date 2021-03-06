#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 02 June 2020 15:29:22
# Last Modified time: Tue 16 June 2020 14:37:47 

# Description:
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    """Class Testing Views in Home App"""

    def setUp(self):
        """Set Up variables used in this test"""
        self.client = Client()
        self.home_url = reverse('home')
        self.legal_url = reverse('legal')

    # Testing Function based views
    def test_home_GET(self):
        """Testing the home() GET method"""
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')

    def test_legal_GET(self):
        """Testing the home() GET method"""
        response = self.client.get(self.legal_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/legal.html')
