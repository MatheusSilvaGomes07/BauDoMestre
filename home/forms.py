from django import forms
from .models import Campanha, Perfil

# Forms da Campanha
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

# Forms do Perfil do usuário
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['fotoConta', 'idade', 'descricao', 'tipo_sessao', 'tipo_player', 'sistema_rpg']
        labels = {
            'fotoConta': 'Insira a foto de usuário',
            'descricao': 'Descrição da conta:',
            'sistema_rpg': 'Sistema de RPG preferido:',
            'tipo_sessao': 'Tipo de sessão:',
            'tipo_player': 'Tipo de player:',
            'idade': 'Insira sua idade:'
        }

    # Upload da foto do usuário já alterando o nome da imagem
    def save(self, commit=True):
        perfil = super().save(commit=False)

        nova_foto = self.cleaned_data.get('fotoConta', None)
        if nova_foto:
            perfil.fotoConta = nova_foto

        if commit:
            perfil.save()

        return perfil
