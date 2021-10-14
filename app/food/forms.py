from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from . models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name',  'item_desc', 'item_price', 'item_image']

        
        labels = {
            'item_name':'Item Name',
            'item_desc': 'Description',
            'item_price': 'Price',
            'item_image': 'Image Link'
        }
    
        widgets = {
            'item_name': forms.TextInput(attrs={'class':'form-control'}),
            'item_desc': forms.TextInput(attrs={'class':'form-control'}),
            'item_price': forms.TextInput(attrs={'class':'form-control'}),
            'item_image': forms.TextInput(attrs={'class':'form-control', 'placeholder':'copy image link and drag'})
        }