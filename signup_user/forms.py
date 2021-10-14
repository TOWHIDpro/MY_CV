from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from . models import user_profile

# SIGNUP
class SignupForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    
    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'})
        }
# LOGIN
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

# PASS CHANGE
class PasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Old Password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

# LOGIDIN USER PROFILE EDIT
class user_profile_edit(forms.ModelForm):
    # profile_img=forms.FileField(label='Upload image')
    class Meta:
        model = user_profile
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'expert_at': forms.TextInput(attrs={'placeholder': 'Expert At'}),
            'about': forms.TextInput(attrs={'placeholder': 'About'}),
            'age': forms.TextInput(attrs={'placeholder': 'Age'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'language': forms.TextInput(attrs={'placeholder': 'Language'}),
        }