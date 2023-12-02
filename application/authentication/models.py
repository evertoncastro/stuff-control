from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from application.common.models import BaseModel
from .managers import UserManager


class User(AbstractUser, BaseModel):
    username = None
    email = models.EmailField(_("email address"), unique=True, null=False, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    