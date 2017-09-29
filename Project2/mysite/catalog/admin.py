# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from catalog.models import Author, Book

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name', )
	
	
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', )
	
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)

