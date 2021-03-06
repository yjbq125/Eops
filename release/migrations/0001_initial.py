# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-09 22:07
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=128, unique=True, verbose_name='Username')),
                ('role', models.CharField(blank=True, choices=[('Admin', 'Administrator'), ('User', 'User'), ('App', 'Application')], default='User', max_length=10, verbose_name='Role')),
                ('wechat', models.CharField(blank=True, max_length=128, verbose_name='Wechat')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone')),
                ('email', models.EmailField(max_length=128, unique=True, verbose_name='Email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'ordering': ['username'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseList',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('project', models.CharField(max_length=50, verbose_name='project_name')),
                ('modules', models.CharField(max_length=500, verbose_name='modeule_name')),
                ('start_time', models.DateTimeField(auto_now_add=True, verbose_name='Start time')),
                ('release_time', models.DateTimeField(auto_now_add=True, verbose_name='Release time')),
                ('release_status', models.CharField(choices=[('0x01', 'waiting'), ('0x02', 'success'), ('0x03', 'failure')], max_length=10, verbose_name='Status')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
            ],
            options={
                'verbose_name': 'User',
                'ordering': ['id'],
            },
        ),
    ]
