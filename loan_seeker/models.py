from django.db import models
from django.contrib.auth.models import User


class LoanSeeker(models.Model):
    wallet_no = models.AutoField(primary_key=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    gender = models.CharField(max_length=6, default='')
    dob = models.DateField(auto_now=False, auto_now_add=False)
    occupation = models.CharField(max_length=50, default='')
    institution = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=50, default='')
    nid = models.CharField(max_length=17, default='')
    image = models.ImageField(upload_to='images', default='default.png')
    phone = models.CharField(max_length=11, default='')
    address = models.CharField(max_length=100, default='', null=True)

    class Meta:
        db_table = 'Loan_seeker'

    def __str__(self):
        return "%s is a loan-seeker of e-wallet." % self.name


class LoanSeekersWallet(models.Model):
    wallet_no = models.OneToOneField(LoanSeeker, on_delete=models.CASCADE, primary_key=True,)
    balance = models.FloatField(default=0.0)
    loan_amount = models.FloatField(default=0.0)
    deadline = models.DateField(auto_now=False, auto_now_add=False, null=True)
    loans_approved = models.IntegerField(default=0.0)

    class Meta:
        db_table = 'Loan_seekers_Wallet'


class Instalments(models.Model):
    wallet_no = models.ForeignKey(LoanSeeker, on_delete=models.PROTECT, db_column='Loan_seekers_wallet')
#    loan_id = models.ForeignKey(CentralWallet, on_delete=models.CASCADE)
    instalment_no = models.IntegerField(default=0)
    instalment = models.FloatField(default=0.0)
    payment = models.FloatField(default=0.0)
    payment_due = models.FloatField(default=0.0)
    payment_date = models.DateField(auto_now=False, auto_now_add=False)
    status = models.TextField()

    class Meta:
        db_table = 'Instalments'