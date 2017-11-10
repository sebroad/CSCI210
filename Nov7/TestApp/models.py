# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Song(models.Model):
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    def __str__(self):
        return self.title


