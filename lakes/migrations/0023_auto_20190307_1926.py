# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-03-07 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lakes', '0022_auto_20181129_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trailhead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='lake',
            name='traildistance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='lake',
            name='trailhead',
            field=models.ManyToManyField(blank=True, to='lakes.Trailhead'),
        ),
    ]
