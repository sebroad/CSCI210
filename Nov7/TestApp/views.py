# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, loader
from django.http import HttpResponse
from TestApp.models import *

# Create your views here.
def home(request):
    songs = Song.objects.all()
    t = loader.get_template('home.html')
    c = dict({'songs': songs})
    return HttpResponse(t.render(c))

