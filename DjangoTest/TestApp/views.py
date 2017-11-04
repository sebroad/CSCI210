# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, loader
from django.http import HttpResponse
from TestApp.models import *

# Create your views here.
def home(request):
	
	if 'search' in request.GET:
		search = request.GET['search']
	else:
		search = 'xxx'
	
	zips = ZipCode.objects.filter(zip__startswith=search)
	if len(zips) == 0:
		zips = ZipCode.objects.filter(state__abbr=search)
	if len(zips) == 0:
		zips = ZipCode.objects.filter(state__name=search)
	if len(zips) == 0:
		zips = ZipCode.objects.filter(city__name__contains=search)
		
	c = dict({'zips': zips})

	t = loader.get_template('zip.html')
	
	return HttpResponse(t.render(c))

def zip(request):
	
	zip = request.path.replace('/zip/','')
	
	zips = ZipCode.objects.filter(zip=zip)

	t = loader.get_template('zip.html')
	c = dict({'zips': zips})
	
	return HttpResponse(t.render(c))

def city(request):
	
	city = request.path.replace('/city/','')
	
	zips = ZipCode.objects.filter(city__name__startswith=city)

	t = loader.get_template('zip.html')
	c = dict({'zips': zips})
	
	return HttpResponse(t.render(c))

def state(request):
	
	state = request.path.replace('/state/','')
	
	zips = ZipCode.objects.filter(state__abbr=state)

	t = loader.get_template('zip.html')
	c = dict({'zips': zips})
	
	return HttpResponse(t.render(c))

