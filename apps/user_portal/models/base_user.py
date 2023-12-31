from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from apps.user_portal.managers.base_user import BaseUserManager


class CallableUser(AbstractBaseUser, PermissionsMixin):
    """
    The CallableUser class allows to get any type of user by calling
    CallableUser.object(email="my@email.dom") or
    CallableUser.objects.filter(email__endswith="@email.dom").select_subclasses()
    """

    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    password = None
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)

    objects = BaseUserManager()


class AbstractUser(CallableUser):
    """
    Here are the fields that are shared among specific User subtypes.
    Making it abstract makes 1 email possible in each User subtype.
    """

    is_superuser = None

    objects = BaseUserManager()

    def __unicode__(self):

        return self.email

    class Meta:
        abstract = True
