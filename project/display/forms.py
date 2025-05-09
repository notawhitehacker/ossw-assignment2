from django import forms

class CreditForm(forms.Form) :
    credit = forms.IntegerField(min_value=1, max_value=5)
    