# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import loader, render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
	books = Book.objects.all()
	authors = Author.objects.all()
	for book in books:
		print book.title
	t = loader.get_template('home.html')
	c = dict({'books': books, 'authors': authors})
	return HttpResponse(t.render(c))
	
def titles(request):
	title = request.path.replace('/titles/', '')
	
	return HttpResponse(title)
	
def authors(request):
	return HttpResponse()
	
def query(request):
	return HttpResponse()
