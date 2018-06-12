from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    ROLE_ADMIN = 'Admin'
    ROLE_USER = 'User'
    ROLE_APP = 'App'

    ROLE_CHOICES = (
        (ROLE_ADMIN, _('Administrator')),
        (ROLE_USER, _('User')),
        (ROLE_APP, _('Application'))
    )

    username = models.CharField(
        max_length=128, unique=True, verbose_name=_('Username')
    )
    role = models.CharField(
        choices=ROLE_CHOICES, default='User', max_length=10,
        blank=True, verbose_name=_('Role')
    )
    wechat = models.CharField(
        max_length=128, blank=True, verbose_name=_('Wechat')
    )
    phone = models.CharField(
        max_length=20, blank=True, null=True, verbose_name=_('Phone')
    )
    email = models.EmailField(
        max_length=128, unique=True, verbose_name=_('Email')
    )

    class Meta:
        ordering = ['username']
        verbose_name = _("User")

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
        ('0x001', 'waiting'),
        ('0x002', 'success'),
        ('0x003', 'failure')
    )

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    project =  models.CharField(max_length=50, verbose_name='project_name')
    modules = models.CharField(max_length=500, verbose_name='modeule_name')
    start_time = models.DateTimeField(auto_now_add=True, verbose_name=_('Start time'))
    release_time = models.DateTimeField(auto_now_add=True, verbose_name=_('Release time'))
    release_status = models.CharField(choices=ROLE_CHOICES, max_length=10, verbose_name=_('Status'))
    comment = models.TextField(verbose_name=_('Comment'), blank=True)











