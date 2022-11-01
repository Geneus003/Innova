from django import forms

class reg_f(forms.Form):
    mail = forms.CharField(max_length=128, required=True)
    name = forms.CharField(max_length=64, required=True)
    password = forms.CharField(max_length=64, required=True)
    surname = forms.CharField(max_length=64, required=True)