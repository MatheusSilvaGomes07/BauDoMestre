from django import forms
from .models import Pasta, File

class PastaForm(forms.ModelForm):
    class Meta:
        model = Pasta
        fields = '__all__'
        exclude = ['owner', 'divisao']

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'
        exclude = ['owner', 'pasta']