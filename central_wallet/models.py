from django.db import models
from loan_seeker.models import LoanSeekersWallet
from investor.models import InvestorsWallet


class CentralWallet(models.Model):
    loan_id = models.AutoField(primary_key=True)
    wallet_id = models.ForeignKey(LoanSeekersWallet, on_delete=models.CASCADE)
    loan_amount = models.FloatField(default=0.0)
    interest_rate = models.FloatField(default=1.0)

    class Meta:
        db_table = 'Central_Wallet'


class Transactions(models.Model):
    serial_no = models.IntegerField(primary_key=True)
    user_type = models.CharField(max_length=11, db_column='User', default='')
    transaction_type = models.CharField(max_length=20, default='')
    transaction_amount = models.FloatField(default=0.0)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    remarks = models.TextField(default='')


    class Meta:
        db_table = 'Transactions'


class LoanLog(models.Model):
    loan_id = models.ForeignKey(CentralWallet, on_delete=models.CASCADE)
    member_id = models.ForeignKey(InvestorsWallet, on_delete=models.CASCADE)
    provided_amount = models.FloatField(default=0.0)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    profit_amount = models.FloatField(default=0.0)

    class Meta:
        db_table = 'Loan_Log'