from django import forms
from .models import Map, Token, DnDCampanha, OrdemParanormalCampanha, CallOfCthulhuCampanha, TormentaCampanha, PastaCriaturas
from meus_personagens.forms import DnDForm, OrdemParanormalForm, TormentaForm, CallOfCthulhuForm

class FileInputWithoutClear(forms.ClearableFileInput):
    template_name = 'principal/custom_file_input.html'
    
class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = ['name', 'image']
        labels = {
            'image': '', 
            'name': ''
        }

class PastaCriaturasForm(forms.ModelForm):
    class Meta:
        model = PastaCriaturas
        fields = ['nome']
        labels = {
            'nome': ''  # Define a label do campo 'nome' como uma string vazia
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite o nome da pasta'})  # Adiciona o placeholder
        }

class TokenForm(forms.ModelForm):
    class Meta:
        model = Token
        fields = ['image']

class CampanhaDnDForm(DnDForm):
    class Meta(DnDForm.Meta):
        model = DnDCampanha
        fields = '__all__'
        labels = {
           #'foto': '',
        }
        widgets = {
            'inventario': forms.Textarea(attrs={'rows': 15, }), #'cols': 15
            'foto': FileInputWithoutClear,
        
        }
        exclude = ['campanha_id', 'nomePerfil', 'pasta']

class CampanhaTormentaForm(TormentaForm):
    class Meta(TormentaForm.Meta):
        model = TormentaCampanha
        exclude = ['campanha_id', 'nomePerfil', 'pasta']

class CampanhaCallOfCthulhuCForm(CallOfCthulhuForm):
    class Meta(CallOfCthulhuForm.Meta):
        model = CallOfCthulhuCampanha
        exclude = ['campanha_id', 'nomePerfil', 'pasta']

class CampanhaOrdemParanormalForm(OrdemParanormalForm):
    class Meta(OrdemParanormalForm.Meta):
        model = OrdemParanormalCampanha
        exclude = ['campanha_id', 'nomePerfil', 'pasta']

