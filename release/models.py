# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.
class User(AbstractUser):
    ROLE_ADMIN = 'Admin'
    ROLE_USER = 'User'

    ROLE_CHOICES = (
        (ROLE_ADMIN, 'Administrator'),
        (ROLE_USER, 'User'),
    )
    username = models.CharField(max_length=128, unique=True, verbose_name='Username')
    role = models.CharField(
        choices=ROLE_CHOICES, default='User', max_length=10,
        blank=True, verbose_name='Role'
    )
    wechat = models.CharField(max_length=128, verbose_name='Wechat')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Phone')
    email = models.EmailField(max_length=128, verbose_name='Email')

    class Meta:
        ordering = ['username']
        verbose_name = "User"

    def __str__(self):
        return self.username

    @property
    def is_superuser(self):
        if self.role == 'Admin':
            return True
        else:
            return False

    @is_superuser.setter
    def is_superuser(self, value):
        if value is True:
            self.role = 'Admin'
        else:
            self.role = 'User'

class ReleaseList(models.Model):
    RELEASE_STATUS = (
        ('0x01', 'waiting'),
        ('0x02', 'success'),
        ('0x03', 'failure')
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    project =  models.CharField(max_length=50, verbose_name='project_name')
    modules = models.CharField(max_length=500, verbose_name='modeule_name')
    start_time = models.DateTimeField(auto_now_add=True, verbose_name='Start time')
    release_time = models.DateTimeField(auto_now_add=True, verbose_name='Release time')
    release_status = models.CharField(choices=RELEASE_STATUS, max_length=10, verbose_name='Status')
    comment = models.TextField(verbose_name='Comment', blank=True)
         
    class Meta:
        ordering = ['id']
        verbose_name = "User"
