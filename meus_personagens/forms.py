from django import forms
from .models import DnD, OrdemParanormal



class DnDForm(forms.ModelForm):
    class Meta:
        model = DnD
        fields = '__all__'
        labels = {
           #'classe': ''
        }
        widgets = {
            'inventario': forms.Textarea(attrs={'rows': 15, }) #'cols': 15
        }
        exclude = ['nomePerfil']
        


class OrdemParanormalForm(forms.ModelForm):
    class Meta:
        model = OrdemParanormal
        fields = ['nome', 'nex']
