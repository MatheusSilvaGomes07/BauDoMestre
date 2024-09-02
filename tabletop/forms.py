from django import forms
from .models import Map, Token

class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = ['name', 'image']

class TokenForm(forms.ModelForm):
    class Meta:
        model = Token
        fields = ['image']
