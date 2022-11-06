from django import forms
from .models import CustomUser


class register(forms.ModelForm):
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'class': 'input', 'placeholder':'Введите почту'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder':'Введите пароль', 'id': 'password'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'Введите имя'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'Введите фамилию'}))

    REQUIRED_FIELDS = ['email', 'password', 'first_name', 'last_name']

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'last_name')