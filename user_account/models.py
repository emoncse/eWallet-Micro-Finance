from django.db import models
from django.contrib.auth.models import User


class users_account(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    usertype = models.CharField(max_length=50, default='', null=True)

    class Meta:
        db_table = 'users_account'