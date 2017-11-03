# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, loader
from django.http import HttpResponse
from TestApp.models import *

# Create your views here.
def home(request):
	if 'search' in request.GET:
		zip = request.GET['search']
		city = request.GET['search']
		state = request.GET['search']
	else:
		zip = '000'
		city = 'xxx'
		state = 'XX'
	zips = ZipCode.objects.filter(zip__startswith=zip)
	print len(zips)
	cities = City.objects.filter(name__contains=city)
	states = State.objects.filter(abbr=state)
	t = loader.get_template('home.html')
	c = dict({'zips': zips, 'states': [], 'cities': []})
	return HttpResponse(t.render(c))
