#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 02 June 2020 15:28:18
# Last Modified time: Tue 16 June 2020 22:10:37 

# Description:
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_default.jpg',
                              upload_to='profile_pics')
    accord_de_don_des_données_à_la_recherche_médicale = models.BooleanField(
        null=False, default=False)

    # Add here more field (added on top of User's model)
    # to appear in profile e.g. Bio, City, langage, etc

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
