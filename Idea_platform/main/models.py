from django.db import models

# Create your models here.


class Users(models.Model):
    mail = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64)
    birthday = models.DateTimeField()
    root = models.BooleanField(default=False)

class Users2(models.Model):
    mail = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    root = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    
