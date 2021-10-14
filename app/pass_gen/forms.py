from django import forms
from django.forms import widgets
from django.forms.forms import Form

class PassForm(forms.Form):
    lenchoice =(
    ("8", "Eight"),
    ("10", "Ten"),
    ("12", "Twelve"),
    ("16", "Sixteen"),
    )
    length = forms.ChoiceField(choices=lenchoice)
    length.widget.attrs.update({'class':'form-control'})

    upper = forms.BooleanField(label='Uppercase',)
    numbers = forms.BooleanField(label='Numbers')
    char = forms.BooleanField(label='Special Characters')

    