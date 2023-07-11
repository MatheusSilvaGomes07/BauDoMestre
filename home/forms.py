from django import forms
from .models import Campanha

class CampanhaForm(forms.ModelForm):
    class Meta:
        model = Campanha
        fields = ['nomeCampanha', 'sistemaCampanha', 'descricaoCampanha', 'fotoCampanha', 'ambienteCampanha', 'numeroJogadores', 'diasSessao', 'generoRPG']
        labels = {
            'nomeCampanha': 'Nome da Campanha',
            'sistemaCampanha': 'Sistema de RPG',
            'descricaoCampanha': 'Descrição',
            'fotoCampanha': 'Foto da Campanha',
            'ambienteCampanha': 'Ambiente de RPG',
            'numeroJogadores': 'Número de Jogadores',
            'diasSessao': 'Dias da Sessão',
            'generoRPG': 'Gênero de RPG',
        }
