from django.contrib.auth.models import User
from django.db import models


class Investor(models.Model):
    wallet_no = models.AutoField(primary_key=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    gender = models.CharField(max_length=6, default='')
    dob = models.DateField(auto_now=False, auto_now_add=False, default='0000-00-00')
    occupation = models.CharField(max_length=50, default='')
    institution = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=50, default='')
    nid = models.CharField(max_length=17, default='')
    image = models.ImageField(upload_to='images', default='default.png')
    phone = models.CharField(max_length=11, default='')
    address = models.CharField(max_length=100, default='')

    class Meta:
        db_table = 'Investor'

    def __str__(self):
        return "%s is a Investor of e-wallet." % self.name


class InvestorsWallet(models.Model):
    wallet_no = models.OneToOneField(
        Investor,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    # wallet_no = models.ForeignKey(Investor, on_delete=models.CASCADE, primary_key=True)
    balance = models.FloatField(default=0.0)
    fixed_savings = models.FloatField(default=0.0)
    profit = models.FloatField(default=0.0)
    last_deposit = models.FloatField(default=0.0)
    deposit_date = models.DateField(auto_now=False, auto_now_add=False, default='0000-00-00')
    loans_approved = models.IntegerField(default=0)
    loan_amount = models.FloatField(default=0.0)

    class Meta:
        db_table = 'Investors_wallet'
