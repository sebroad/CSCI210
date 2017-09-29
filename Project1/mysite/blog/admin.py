# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import BlogPost

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('timestamp', 'title')

admin.site.register(BlogPost,BlogPostAdmin)