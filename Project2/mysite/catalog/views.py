# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import loader, render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
	books = Book.objects.all()
	authors = Author.objects.all()
	t = loader.get_template('home.html')
	c = dict({'books': books, 'authors': authors})
	return HttpResponse(t.render(c))
	
def titles(request, title):
	books = Book.objects.filter(title__contains=title)
	t = loader.get_template('titles.html')
	c = dict({'books': books})
	return HttpResponse(t.render(c))
	
def authors(request):
	author = request.path.replace('/authors/', '')
	authors = Author.objects.filter(name__contains = author)
	books = Book.objects.filter(author__name__contains = author)
	t = loader.get_template('authors.html')
	c = dict({'books': books, 'authors': authors})
	return HttpResponse(t.render(c))

	
def query(request):
	params = request.GET
	data = dict()
	if 'title' in params:
		books = Book.objects.filter(title__contains=params['title'])
		data['books'] = list()
		for b in books:
			book = dict()
			book['title']=b.title
			book['pubdate']=str(b.pubdate)
			book['publisher']=b.publisher
			
			data['books'].append(book)
			
	return HttpResponse(json.dumps(data))
