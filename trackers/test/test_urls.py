#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 02 June 2020 15:29:22
# Last Modified time: Mon 19 October 2020 22:09:27 

# Description:

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from trackers.views import pain_tracker, digest_tracker


class TestUrls(SimpleTestCase):
    """Class URLs Test - TestUrls"""

    def test_pain(self):
        url = reverse('douleurs')
        self.assertEquals(resolve(url).func, pain_tracker)

    def test_digest(self):
        url = reverse('digestif')
        self.assertEquals(resolve(url).func, digest_tracker)
