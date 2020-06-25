from django import forms
from django.contrib.auth.models import User

from .models import Profil

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProfilEditForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ('photo','nama')


