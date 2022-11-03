from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Commands(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)


class Ideas(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    release_date = models.DateField(auto_now_add=True)
    command_id = models.ForeignKey(Commands, default=None, on_delete=models.CASCADE)

    
