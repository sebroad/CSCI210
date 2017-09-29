# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=100)
	dead = models.BooleanField(default=False)
	def __unicode__(self):
		return unicode(self.name)

class Book(models.Model):
	title = models.CharField(max_length=200)
	author = models.ManyToManyField(Author)
	

