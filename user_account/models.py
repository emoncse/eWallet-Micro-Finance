from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.forms import forms


class users_account(models.Model):
    username = models.CharField(max_length=15, primary_key=True)
    usertype = models.CharField(max_length=50, default='', null=True)
    name = models.CharField(max_length=50, default='', null=True)
    email = models.CharField(max_length=60, default='', null=True)
    gender = models.CharField(max_length=11, default='', null=True)
    occupation = models.EmailField(max_length=50, default='', null=True)
    institution = models.CharField(max_length=100, default='', null=True)
    dob = models.DateTimeField(null=True)
    nid = models.CharField(max_length=17, default='', null=True)
    address = models.CharField(max_length=100, default='', null=True)
    phone = models.CharField(max_length=11, default='', null=True)
    image = models.ImageField(upload_to='images', default='default.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')

    class Meta:
        db_table = 'users_account'