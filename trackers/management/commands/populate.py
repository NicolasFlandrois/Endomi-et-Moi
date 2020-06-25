#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Thu 25 June 2020 16:07:17
# Last Modified time: Thu 25 June 2020 16:11:58 

# Description:

from django.core.management.base import BaseCommand, CommandError
import json
from trackers.models import Constants


class Command(BaseCommand):
    help = """This function will update the products' database,
    from constants.json file, placed in project's root directory."""

    def handle(self, *args, **options):
        """
        This function will update the trackers_constants' database,
        from constants.json file.
        """
        try:
            print(
                "We are checking informations from the new databases settings \
in constants.json.")
            constant = Constants()
            constant.populate()
            print(
                "The update from constants.json is now finished.")

        except:
            raise CommandError('Something went wrong here')
