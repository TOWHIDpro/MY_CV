from django import forms
from django.db.models import fields
from django.forms import widgets
from . models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'id':'nameid'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'id':'emailid'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control', 'id':'passid'}),
            
        }