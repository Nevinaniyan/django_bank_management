from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Account(models.Model):
    account_number = models.TextField(max_length=20, unique=True)
    account_holder_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.account_holder_name



class Transaction(models.Model):
    # TRANSACTION_TYPES = (
    #     ('deposit', 'Deposit'),
    #     ('withdrawal', 'Withdrawal'),
    # )

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20)                 # , choices=TRANSACTION_TYPES
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

        # return f"{self.transaction_type} of {self.amount} on {self.date}"
