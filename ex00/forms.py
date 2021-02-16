from django import forms
from django.forms import ModelForm
from .models import MyUsers

class SignUpForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    password_verif = forms.CharField(widget=forms.PasswordInput)

class SignInForm(forms.ModelForm):
    class Meta:
        model = MyUsers
        fields = ('username', 'password')