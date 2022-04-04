from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
   email = models.EmailField('email address', unique=True)
   image = models.ImageField(upload_to='profile_image', null=True, blank=True)
   about_me = models.TextField(blank=True)
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ["username"]
