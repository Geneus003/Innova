from django.db import models

# Create your models here.


class Users(models.Model):
    mail = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64)
    birthday = models.DateTimeField()
    root = models.BooleanField(default=False)

