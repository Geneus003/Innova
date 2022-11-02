from django import forms
from django.contrib.auth.models import User
from .models import CustomUser

class reg_f(forms.Form):
    mail = forms.CharField(max_length=128, required=True)
    name = forms.CharField(max_length=64, required=True)
    password = forms.CharField(max_length=64, required=True)
    surname = forms.CharField(max_length=64, required=True)


class register(forms.ModelForm):
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'class': 'input', 'placeholder':'Введите почту'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder':'Введите пароль', 'id': 'password'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'Введите имя'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'Введите фамилию'}))

    REQUIRED_FIELDS = ['email', 'password', 'first_name', 'last_name']

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'last_name')

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError('Passwords don\'t match.')
    #     return cd['password2']