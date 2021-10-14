from django import forms
from . models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'discreption', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'discreption': forms.Textarea(attrs={'class':'form-control'}),
        }