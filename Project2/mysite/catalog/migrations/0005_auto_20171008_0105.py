# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_author_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='book',
            name='pagecount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='pubdate',
            field=models.DateTimeField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(default='', max_length=100),
        ),
    ]
