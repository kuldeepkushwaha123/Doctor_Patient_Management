from account.manager import UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin
# Create your models here.

class User(AbstractUser):
    category = (
        ('Doctor', 'Doctor'),
        ('Patient', 'Patient'),
    )
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    profile_picture=models.ImageField(null=True,blank=True,upload_to="upload/")
    level=models.CharField(max_length=10,choices=category)
    address = models.CharField(max_length=80)

    username=models.CharField(max_length=30,unique=True)
    address=models.CharField(max_length=30)
    email=models.EmailField(_('Email Address'),unique=True)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=UserManager()
    
    
    
    