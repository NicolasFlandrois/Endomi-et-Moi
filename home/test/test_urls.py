#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 02 June 2020 15:29:22
# Last Modified time: Tue 16 June 2020 14:37:51 

# Description:

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import home, legal


class TestUrls(SimpleTestCase):
    """Class Test - TestUrls"""

    def test_home(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_legal(self):
        url = reverse('legal')
        self.assertEquals(resolve(url).func, legal)
