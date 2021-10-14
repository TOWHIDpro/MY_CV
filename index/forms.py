from django import forms
from django.forms import widgets
from . models import M_message

class MessageForm(forms.ModelForm):
    class Meta:
        model = M_message
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'sub':forms.TextInput(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control'}),
        }