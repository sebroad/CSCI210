# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from TestApp.models import *

# Register your models here.
class ZipCodeAdmin(admin.ModelAdmin):
	list_display = ('zip', )
		
admin.site.register(ZipCode, ZipCodeAdmin)

