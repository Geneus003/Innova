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

    
class Categories(models.Model):
    name = models.CharField(max_length=255)


class Ideas(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    release_date = models.DateTimeField(auto_now_add=True)
    moderated = models.IntegerField(default=2)
    published = models.BooleanField(default=True)


class Tags(models.Model):
    name = models.CharField(max_length=255)


class IdeasTags(models.Model):
    idea_id = models.ForeignKey(Ideas, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tags, on_delete=models.CASCADE)


class AuthorIdeas(models.Model):
    author_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    idea_id = models.ForeignKey(Ideas, on_delete=models.CASCADE)


class AuthorCommands(models.Model):
    author_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    command_id = models.ForeignKey(Commands, on_delete=models.CASCADE)
