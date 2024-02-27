from django import forms
from .models import DnD, OrdemParanormal, Tormenta, CallOfCthulhu

class FileInputWithoutClear(forms.ClearableFileInput):
    template_name = 'principal/custom_file_input.html'

class DnDForm(forms.ModelForm):
    class Meta:
        model = DnD
        fields = '__all__'
        labels = {
           #'foto': '',
        }
        widgets = {
            'inventario': forms.Textarea(attrs={'rows': 15, }), #'cols': 15
            'foto': FileInputWithoutClear,
        
        }
        exclude = ['nomePerfil']
        
        


class OrdemParanormalForm(forms.ModelForm):
    class Meta:
        model = OrdemParanormal
        fields = '__all__'
        exclude = ['nomePerfil']
        widgets = {
            'foto': FileInputWithoutClear,
        }


class TormentaForm(forms.ModelForm):
    class Meta:
        model = Tormenta
        fields = '__all__'
        exclude = ['nomePerfil']
        widgets = {
            'foto': FileInputWithoutClear,
        }


class CallOfCthulhuForm(forms.ModelForm):
    class Meta:
        model = CallOfCthulhu
        field = '__all__'
        exclude = ['nomePerfil']
        widgets = {
            'foto': FileInputWithoutClear,
        }