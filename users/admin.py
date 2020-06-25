#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 02 June 2020 15:28:15
# Last Modified time: Thu 25 June 2020 10:02:35 

# Description:

from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
