from django import forms
from .models import Campanha, Perfil


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

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['fotoConta', 'descricao', 'tipo_sessao', 'tipo_player', 'sistema_rpg']
        labels = {
            'fotoConta': 'Insira a foto de usuário',
            'descricao': 'Descrição da conta:',
            'sistema_rpg': 'Sistema de RPG preferido:',
            'tipo_sessao': 'Tipo de sessão:',
            'tipo_player': 'Tipo de player:',
        }
