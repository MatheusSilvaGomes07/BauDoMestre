from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import PermissionDenied
from django.db.models import Q

from meus_personagens.models import CallOfCthulhu, DnD, OrdemParanormal, Tormenta
from tabletop.models import CallOfCthulhuCampanha, DnDCampanha, OrdemParanormalCampanha, TormentaCampanha
from .models import Campanha, Perfil
from .forms import CampanhaForm, PerfilForm, CustomSignupForm, CustomLoginForm
from functools import wraps
from chat.models import Grupo, SolicitacaoEntrada
from SistAmizade.models import Amigo, SolicitacaoAmizade
from random import randint
import os
import shutil
from allauth.account.views import SignupView, LoginView # type: ignore

class CustomSignupView(SignupView):
    form_class = CustomSignupForm
    def form_invalid(self, form):
        # Reexibe o formulário com mensagens de erro
        return self.render_to_response(self.get_context_data(form=form))

class CustomLoginView(LoginView):
    form_class = CustomLoginForm



def apenas_mestre(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        campanha = get_object_or_404(Campanha, id=kwargs['campanha_id'])
        perfil = Perfil.objects.get(nomePerfil=request.user)

        if campanha.nomeMestre == perfil:
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied("Você não tem permissão para realizar esta ação.")

    return _wrapped_view


#Renomear imagem de perfil

def renomear_foto_perfil(nome_de_conta, nova_foto):
    # Obtém o nome do arquivo original da nova foto
    nome_original = nova_foto.name

    # Obtém a extensão do arquivo original
    extensao = os.path.splitext(nome_original)[1]

    # Constrói o novo nome de arquivo com base no nome da conta e a extensão do arquivo original
    novo_nome_arquivo = f"{nome_de_conta}{extensao}"

    # Obtém o diretório de destino onde a foto deve ser movida
    destino = os.path.join(settings.MEDIA_ROOT, 'static', 'img', 'fotoUser', novo_nome_arquivo)

    # Salva a nova foto com o novo nome no diretório de destino usando shutil
    with open(nova_foto.path, 'rb') as origem_arquivo:
        with open(destino, 'wb+') as destino_arquivo:
            shutil.copyfileobj(origem_arquivo, destino_arquivo)

    # Retorna o novo nome do arquivo para atualizar o campo 'fotoConta' no modelo Perfil
    return novo_nome_arquivo



# Decorator manual feito para impedir que não mestres entrem no link pela url
def jogadores_permitidos(required_types):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            perfil = Perfil.objects.get(nomePerfil=request.user)
            if perfil.tipo_player in required_types:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('buscarmesa')
        return _wrapped_view
    return decorator

# Tela de 404
def handler404(request, exception):
    aleatorio = randint(1, 6)
    return render(request, 'principal/404.html', {'aleatorio': aleatorio})

# view da home
def index(request):
    if isinstance(request.user, AnonymousUser):
        return render(request, 'principal/home-ia.html')
    else:
        user = request.user
        perfil = Perfil.objects.get(nomePerfil=user)
        fotoConta = Perfil.objects.get(id=user.id).fotoConta
        grupos = None


        #Isso é uma maneira muito burra de conciliar os personagens de Campanha com MeusPersonagens mas é o que ta tendo para hoje
        ids_campanha_T = TormentaCampanha.objects.values_list('pk', flat=True).distinct()
        ids_campanha_D = DnDCampanha.objects.values_list('pk', flat=True).distinct()
        ids_campanha_O = OrdemParanormalCampanha.objects.values_list('pk', flat=True).distinct()
        ids_campanha_C = CallOfCthulhuCampanha.objects.values_list('pk', flat=True).distinct()


        dnd = DnD.objects.filter(nomePerfil=user).exclude(id__in=ids_campanha_D)
        ordem = OrdemParanormal.objects.filter(nomePerfil=user).exclude(id__in=ids_campanha_O)
        tormenta20 = Tormenta.objects.filter(nomePerfil=user).exclude(id__in=ids_campanha_T)
        coc = CallOfCthulhu.objects.filter(nomePerfil=user).exclude(id__in=ids_campanha_C)

        campanhas = Campanha.objects.filter(chats__membros=user)

        for camp in campanhas:
            uuid = Grupo.objects.get(campanha=camp.id)
            if uuid:
                camp.uuid = uuid.uuid

        for campanha in campanhas:
            grupos = campanha.chats.all()
            for grupo in grupos:
                envioSolicitacao = '1' if bool(SolicitacaoEntrada.objects.filter(de_usuario = request.user.id, para_campanha = campanha.id, status='Pendente')) else '0'

                grupo.envioSolicitacao = envioSolicitacao

        return render(request, 'principal/home.html', {
            'campanhas': campanhas,
            'fotoConta': fotoConta,
            'dnd': dnd,
            'ordem': ordem,
            'tormenta20': tormenta20,
            'coc': coc,
            'perfil': perfil,
            'grupos': grupos})


# views do mural logado + buscar as mesas
@login_required
def buscarmesa(request):
    perfil = Perfil.objects.get(nomePerfil=request.user)
    sistema_busca = request.GET.get('q')
    sistema_filtro = request.GET.get('sistema')
    ambiente_filtro = request.GET.get('ambiente')
    genero_filtro = request.GET.get('genero')
    campanhas = Campanha.objects.all()


    if sistema_busca:
        campanhas = campanhas.filter(Q(nomeCampanha__icontains=sistema_busca))
    if sistema_filtro:
        campanhas = campanhas.filter(Q(sistemaCampanha__icontains=sistema_filtro))
    if ambiente_filtro:
        campanhas = campanhas.filter(Q(ambienteCampanha__icontains=ambiente_filtro))
    if genero_filtro:
        campanhas = campanhas.filter(Q(generoRPG__icontains=genero_filtro))

    campanhas_e_grupos = {}
    for campanha in campanhas:
        grupos = campanha.chats.all()
        for grupo in grupos:
            envioSolicitacao = '1' if bool(SolicitacaoEntrada.objects.filter(de_usuario = request.user.id, para_campanha = campanha.id, status='Pendente')) else '0'

            grupo.envioSolicitacao = envioSolicitacao
        campanhas_e_grupos[campanha] = grupos


    return render(request, 'principal/muralLogado.html', {'campanhas_e_grupos': campanhas_e_grupos, 'perfil': perfil, 'fotoConta': perfil.fotoConta})

@login_required
@apenas_mestre
def excluir_jogador(request, campanha_id, jogador_id):
    campanha = get_object_or_404(Campanha, id=campanha_id)
    jogador = get_object_or_404(Perfil, id=jogador_id)

    grupo = Grupo.objects.get(campanha=campanha)

    # Remover o jogador do grupo da campanha
    grupo.membros.remove(jogador.nomePerfil)

    return redirect('detalhes_campanha', id=campanha_id)

@login_required
@apenas_mestre
def excluir_campanha(request, campanha_id):
    campanha = get_object_or_404(Campanha, id=campanha_id)
    campanha.delete()
    return redirect('buscarmesa')


@login_required
def detalhes_campanha(request, id):
    campanha = get_object_or_404(Campanha, id=id)
    mestre = campanha.nomeMestre
    membros_id = Grupo.objects.filter(campanha=campanha.id).values_list('membros', flat=True)
    membros = Perfil.objects.filter(nomePerfil__in=membros_id)
    user = request.user
    fotoConta = Perfil.objects.get(id=user.id).fotoConta
    grupos = Grupo.objects.filter(campanha=campanha.id)


    return render(request, 'principal/detalhesCampanha.html', {
        'campanha': campanha,
        'mestre': mestre,
        'membros': membros,
        'user': user,
        'fotoConta': fotoConta,
        'grupos': grupos,
    })

# view da busca de usuários
@login_required
def search_user(request):
    conta_busca = request.GET.get('q')
    perfil = Perfil.objects.get(nomePerfil=request.user)
    users = []
    if conta_busca:
        users = Perfil.objects.filter(
            Q(nomePerfil__username__icontains=conta_busca)
        )

    return render(request, 'principal/buscaUser.html', {'users': users, 'busca_realizada': bool(conta_busca), 'fotoConta': perfil.fotoConta})


# view do perfil com link slug dos usuários
@login_required
def exibir_perfil(request, perfil_slug):
    perfil = get_object_or_404(Perfil, slug=perfil_slug)
    is_self = perfil.nomePerfil == request.user
    is_amigo = not is_self and Amigo.objects.filter(usuario=request.user, amigo=perfil.nomePerfil).exists()
    fotoConta = Perfil.objects.get(nomePerfil=request.user).fotoConta
    solicitacao_pendente = None

    quantidade_amigos = Amigo.objects.filter(usuario=perfil.nomePerfil.id).count()

    if not is_self:
        solicitacao_pendente = SolicitacaoAmizade.objects.filter(de_usuario=request.user, para_usuario=perfil.nomePerfil, aceita=False).first()


    return render(request, 'principal/exibir_perfil.html', {'perfil': perfil, 'is_amigo': is_amigo, 'is_self': is_self, 'solicitacao_pendente': solicitacao_pendente, 'quantidade_amigos':quantidade_amigos, 'fotoConta': fotoConta})

# view da criação de campanhas que também é protegida por um decorator que só permite a entrada de "Mestre" e "Ambos"
@login_required
@jogadores_permitidos(["Mestre", "Ambos"])
def criarCampanhas(request):
    if request.method == 'POST':
        form = CampanhaForm(request.POST, request.FILES)
        if form.is_valid():
            campanha = form.save(commit=False)
            perfil_mestre = get_object_or_404(Perfil, nomePerfil=request.user)
            campanha.nomeMestre = perfil_mestre
            campanha.save()

            # Cria um novo chat (grupo) associado à campanha
            novo_grupo = Grupo.objects.create(criador=request.user, publico=True, campanha=campanha)
            novo_grupo.membros.add(request.user)
            novo_grupo.save()

            return redirect('buscarmesa')
    else:
        form = CampanhaForm()

    return render(request, 'principal/criarMesas.html', {'form': form})


# view da conta do usuário logado
@login_required
def usuario(request):
    perfil = Perfil.objects.get(nomePerfil=request.user)
    campanha = Campanha.objects.filter(nomeMestre=perfil).first()
    user = request.user
    fotoConta = Perfil.objects.get(id=user.id).fotoConta

    quantidade_amigos = Amigo.objects.filter(usuario=request.user.id).count()

    return render(request, 'principal/user.html', {
        'perfil': perfil,
        'campanha': campanha,
        'quantidade_amigos':quantidade_amigos,
        'fotoConta': fotoConta,
        'user': user,})


# view da edição de conta do usuário
@login_required
def editarconta(request):
    user = request.user
    perfil, created = Perfil.objects.update_or_create(nomePerfil=request.user)
    fotoConta = Perfil.objects.get(id=user.id).fotoConta
    foto_antiga = perfil.fotoConta.name

    quantidade_amigos = Amigo.objects.filter(usuario=perfil.nomePerfil).count()

    if request.method == 'POST':
        formPerfil = PerfilForm(request.POST, request.FILES, instance=perfil)
        if formPerfil.is_valid():
            if perfil.fotoConta:
                caminho_arquivo_antigo = os.path.join('media', foto_antiga)
                if foto_antiga != perfil.fotoConta:
                    if foto_antiga == 'Indefinido':
                        pass
                    else:
                        os.remove(caminho_arquivo_antigo)
            formPerfil.save()
            return redirect('usuario')

    else:
        formPerfil = PerfilForm(instance=perfil)

    return render(request, 'principal/editarPerfil.html', {'formPerfil': formPerfil, 'user':user, 'perfil':perfil, 'quantidade_amigos': quantidade_amigos, 'fotoConta': fotoConta,})

@login_required
def is_amigo(request, perfil_slug):
    perfil = get_object_or_404(Perfil, slug=perfil_slug)
    amigo = Perfil.objects.get(nomePerfil=request.user)
    is_amigo = amigo.amigo_set.filter(nomePerfil=perfil.nomePerfil).exists()
    return is_amigo


def aboutus(request):
    return render(request, 'principal/about-us.html')

def home(request):
    return render(request, 'principal/home-ia.html')
