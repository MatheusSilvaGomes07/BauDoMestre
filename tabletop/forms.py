# forms.py
from django import forms
from .models import Object

class ObjectForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = ['name','image']