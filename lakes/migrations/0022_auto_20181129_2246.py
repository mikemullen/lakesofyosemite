# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-29 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lakes', '0021_auto_20181129_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lake',
            name='lakeoutline',
            field=models.FileField(blank=True, upload_to='lakeoutlines'),
        ),
        migrations.AlterField(
            model_name='lake',
            name='locationmap',
            field=models.FileField(blank=True, upload_to='locationmaps'),
        ),
    ]