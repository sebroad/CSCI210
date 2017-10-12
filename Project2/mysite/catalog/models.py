# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=100)
	dead = models.BooleanField(default=False)
	
	email = models.EmailField(max_length=100, default='')
	def __unicode__(self):
		return unicode(self.name)

class Book(models.Model):
	title = models.CharField(max_length=200)
	pubdate = models.DateTimeField(default = "2000-01-01")
	publisher = models.CharField(max_length=100, default='')
	pagecount = models.IntegerField(default=0)
	isbn = models.CharField(max_length=30, default='')
	author = models.ManyToManyField(Author)
	

