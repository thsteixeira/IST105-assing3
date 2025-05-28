from django import forms

class NumbersForm(forms.Form):
    num1 = forms.DecimalField(label='Number 01', min_value=1, decimal_places=0, required=True)
    num2 = forms.DecimalField(label='Number 02', min_value=1, decimal_places=0, required=True)
    num3 = forms.DecimalField(label='Number 03', min_value=1, decimal_places=0, required=True)