# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-16 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lakes', '0016_lake_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lake',
            name='image1',
            field=models.ImageField(null=True, upload_to='static/lake_images'),
        ),
    ]
