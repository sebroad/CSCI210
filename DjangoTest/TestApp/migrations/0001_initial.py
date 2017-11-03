# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-03 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('abbr', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip', models.CharField(max_length=5)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestApp.City')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestApp.State')),
            ],
        ),
    ]
