from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.




class User(AbstractUser):
    USERNAME_MIN_LENGTH = 3
    USERNAME_MAX_LENGTH = 16

    PASSWORD_MIN_LENGTH = 8
    PASSWORD_MAX_LENGTH = 30

    custom_username_validator = None
    
    username = models.CharField(
        _("username"),
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
        validators=[AbstractUser.username_validator,
                    MinLengthValidator(USERNAME_MIN_LENGTH)])
    email = models.EmailField(_('email'), unique=True)
    password = models.CharField(_("password"), max_length=128)