#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 02 June 2020 15:29:22
# Last Modified time: Mon 19 October 2020 22:07:16 

# Description:

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from charts.views import ChartView


class TestUrls(SimpleTestCase):
    """Class Charts Test - TestUrls"""

    def test_ChartView(self):
        url = reverse('graph')
        self.assertEquals(resolve(url).func.view_class, ChartView)
