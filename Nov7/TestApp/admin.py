# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from TestApp.models import Song

# Register your models here.
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'album')

admin.site.register(Song, SongAdmin)

