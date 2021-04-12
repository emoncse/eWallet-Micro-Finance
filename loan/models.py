from django.db import models
from loan_seeker.models import LoanSeekersWallet
from django.contrib.auth.models import User
# Create your models here.


class Loan(models.Model):
    choice = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected')
    ]
    wallet_no = models.ForeignKey(LoanSeekersWallet, on_delete=models.CASCADE)
    loan_amount = models.FloatField(default=0.0)
    loan_approval = models.CharField(max_length=10, choices=choice, default='Pending')
    date = models.DateField(auto_now=False, auto_now_add=False, default='0000-00-00')

    def __str__(self):
        return "%s %s" % (self.wallet_no, self.loan_amount)

    class Meta:
        db_table = "Loan_Application"
