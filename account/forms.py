from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model =User
        fields=fields = ['first_name','last_name','profile_picture','level','username', 'email', 'password1', 'password2','address' ]

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Password','type':'password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Re-Password','type':'password'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Address'}))
    # dob = forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}))

class UpdateForm(forms.ModelForm):
    class Meta:
        model =User
        # fields="__all__"
        # fields=['email','address','username']
        fields = ['id','first_name','last_name','profile_picture','level','username', 'email','address' ]