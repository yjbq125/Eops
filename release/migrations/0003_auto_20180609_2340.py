# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-09 23:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0002_auto_20180609_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=128, verbose_name='Email'),
        ),
    ]
