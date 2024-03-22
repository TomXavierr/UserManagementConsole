from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser):
    username = models.CharField(max_length=55, null=False, blank=False)
    email = models.EmailField(max_length=254, unique=True, null=False, blank=False)
    date_joined = models.DateField(verbose_name="date joined", auto_now_add= True)
    last_login      = models.DateTimeField(verbose_name="last login",auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_blocked      = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)



