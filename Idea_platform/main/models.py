from multiprocessing.reduction import AbstractReducer
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.


# class Users(models.Model):
#     mail = models.CharField(max_length=128)
#     name = models.CharField(max_length=64)
#     surname = models.CharField(max_length=64)
#     second_name = models.CharField(max_length=64)
#     birthday = models.DateTimeField()
#     root = models.BooleanField(default=False)

class Users2(models.Model):
    mail = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    root = models.BooleanField(default=False)


    def __str__(self):
        return self.name

# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     second_name = models.CharField(max_length=64)
#     birthday = models.DateField(blank=True, null=True)

#     # def __str__(self):
#     #     return 'Profile for user {}'.format(self.user.username)

# class CustomUser(AbstractUser):
#     first_name = models.CharField(max_length=30, blank=False)
#     last_name = models.CharField(max_length=30, blank=False)
#     email = models.EmailField(blank=False, unique=True)



# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
