from django import forms
from .models import Map, Token, DnDCampanha, OrdemParanormalCampanha, CallOfCthulhuCampanha, TormentaCampanha, PastaCriaturas
from meus_personagens.forms import DnDForm, OrdemParanormalForm, TormentaForm, CallOfCthulhuForm

class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = ['name', 'image']

class PastaCriaturasForm(forms.ModelForm):
    class Meta:
        model = PastaCriaturas
        fields = ['nome']

class TokenForm(forms.ModelForm):
    class Meta:
        model = Token
        fields = ['image']

class CampanhaDnDForm(DnDForm):
    class Meta(DnDForm.Meta):
        model = DnDCampanha
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

