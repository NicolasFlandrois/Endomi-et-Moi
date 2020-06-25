#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 16 June 2020 14:23:33
# Last Modified time: Thu 25 June 2020 12:07:31 

# Description: Allowing to manage database's constants from admin console

from django.contrib import admin
from .models import *

admin.site.register(Constants)
