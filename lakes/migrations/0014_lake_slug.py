# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-13 18:58
from __future__ import unicode_literals

from django.db import migrations, models

from django.utils.text import slugify


def create_name_slug(apps, schema_editor):
    Lake = apps.get_model('lakes', 'Lake')
    for lake in Lake.objects.all():
        lake.slug = slugify(lake.name)
        lake.save()


class Migration(migrations.Migration):

    dependencies = [
        ('lakes', '0011_auto_20181031_1654'),
    ]

    operations = [
        migrations.RunPython(create_name_slug),
    ]