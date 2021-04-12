from django.db import models
from loan_seeker.models import LoanSeekersWallet
# Create your models here.


class Loan(models.Model):
    wallet_no = models.ForeignKey(LoanSeekersWallet, on_delete=models.CASCADE)
    loan_amount = models.FloatField(default=0.0)
    loan_approval = models.BooleanField(default=False)
    date = models.DateField(auto_now=False, auto_now_add=False, default='0000-00-00')

    class Meta:
        db_table = "Loan_Application"
