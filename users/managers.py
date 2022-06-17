from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError(_('Email field cannot be blank!'))

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()

        return user

    
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is False:
            raise ValueError(_('is_staff for superuser must be True!'))

        if kwargs.get('is_superuser') is False:
            raise ValueError(_('is_superuser for superuser must be True!'))

        return self.create_user(email, password, **kwargs)