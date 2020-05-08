from django import forms

class Form(forms.Form):
    company_name = forms.CharField(required=True)
    fiber_cost = forms.IntegerField(required=True)