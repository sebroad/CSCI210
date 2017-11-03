# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class City(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return str(self.name)

class State(models.Model):
	name = models.CharField(max_length=40)
	abbr = models.CharField(max_length=3)
	def __str__(self):
		return str(self.name)

class ZipCode(models.Model):
	zip = models.CharField(max_length=5)
	city = models.ForeignKey(City)
	state = models.ForeignKey(State)
	
