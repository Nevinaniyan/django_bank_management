from django import forms
from account.models import Account
from django import forms


class Accountform(forms.ModelForm):
    class Meta:
        model=Account
        fields="__all__"

      ##  or

        # fields=['title','author']   # or we can give our desired field so that it doesnt takes all fields

      ## or

        # exclude=['price']   # not taking price field and rest all field taking