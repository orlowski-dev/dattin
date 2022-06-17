from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from . import managers
from django.dispatch import receiver
from django.db.models.signals import post_save

def user_dir_path(instance, filename):
    import string, random

    file_ext = filename.split('.')[-1]
    filename = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(0, 19)) + '.' + file_ext

    return f'uploads/profile_{instance.id}/{filename}'

class User(AbstractUser):
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    username = None
    last_name = None

    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name=_('Email address')
    )

    date_of_birth = models.DateField(
        auto_now_add=False,
        verbose_name=_('Date of birth'),
        null=True,
        blank=True,
    )
    location = models.CharField(
        max_length=254,
        verbose_name=_('Location'),
        null=True,
        blank=True,
    )
    profile_picture = models.FileField(
        null=True,
        blank=True,
        verbose_name=_('Profile picture'),
        upload_to=user_dir_path,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = managers.UserManager()

    def __str__(self) -> str:
        return self.email
