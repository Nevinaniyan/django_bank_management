from django.contrib import admin
from account.models import Account
from account.models import Transaction


# Register your models here.

admin.site.register(Account)
admin.site.register(Transaction)