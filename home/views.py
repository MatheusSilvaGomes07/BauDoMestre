from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Campanha, Perfil
from .forms import CampanhaForm, PerfilForm
from django.db.models import Q
from functools import wraps
from chat.models import Mensagem, Grupo
from SistAmizade.models import Amigo
from random import randint
import os
import shutil
from allauth.account.views import SignupView, LoginView
from .forms import CustomSignupForm, CustomLoginForm
from django.contrib import messages

class CustomSignupView(SignupView):
    form_class = CustomSignupForm
    def form_invalid(self, form):
        # Reexibe o formulário com mensagens de erro
        return self.render_to_response(self.get_context_data(form=form))

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    
    

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
    return render(request, 'principal/home.html')

# view do mural não logado
def mural(request):
    campanhas = Campanha.objects.all()
    return render(request, 'principal/mural.html', {'campanhas': campanhas})

# views do mural logado + buscar as mesas
@login_required
def buscarmesa(request):
    perfil = Perfil.objects.get(nomePerfil=request.user)
    sistema_busca = request.GET.get('q')
    sistema_filtro = request.GET.get('sistema')
    ambiente_filtro = request.GET.get('ambiente')
    genero_filtro = request.GET.get('genero')
    campanhas = Campanha.objects.all()
    grupos = Grupo.objects.all()


    if sistema_busca:
        campanhas = campanhas.filter(
            Q(nomeCampanha__icontains=sistema_busca)
        )
    if sistema_filtro:
        campanhas = campanhas.filter(
            Q(sistemaCampanha__icontains=sistema_filtro)
        )
    if ambiente_filtro:
        campanhas = campanhas.filter(
            Q(ambienteCampanha__icontains=ambiente_filtro)
        )
    if genero_filtro:
        campanhas = campanhas.filter(
            Q(generoRPG__icontains=genero_filtro)
        )

    return render(request, 'principal/muralLogado.html', {'campanhas': campanhas, 'perfil': perfil, 'grupos': grupos})


# view da busca de usuários
@login_required
def search_user(request):
    conta_busca = request.GET.get('q')
    users = []
    if conta_busca:
        users = Perfil.objects.filter(
            Q(nomePerfil__username__icontains=conta_busca)
        )
    return render(request, 'principal/buscaUser.html', {'users': users, 'busca_realizada': bool(conta_busca)})


# view do perfil com link slug dos usuários
@login_required
def exibir_perfil(request, perfil_slug):
    perfil = get_object_or_404(Perfil, slug=perfil_slug)
    is_self = perfil.nomePerfil == request.user
    is_amigo = not is_self and Amigo.objects.filter(usuario=request.user, amigo=perfil.nomePerfil).exists()
    
    return render(request, 'principal/exibir_perfil.html', {'perfil': perfil, 'is_amigo': is_amigo, 'is_self': is_self})

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
            return redirect('buscarmesa')
    else:
        form = CampanhaForm()

    return render(request, 'principal/criarMesas.html', {'form': form})


# view da conta do usuário logado
@login_required
def usuario(request):
    perfil = Perfil.objects.get(nomePerfil=request.user)
    return render(request, 'principal/user.html', {'perfil': perfil})


# view da edição de conta do usuário
@login_required
def editarconta(request):
    perfil, created = Perfil.objects.update_or_create(nomePerfil=request.user)
    foto_antiga = perfil.fotoConta.name

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

    return render(request, 'principal/editarPerfil.html', {'formPerfil': formPerfil})

@login_required
def is_amigo(request, perfil_slug):
    perfil = get_object_or_404(Perfil, slug=perfil_slug)
    amigo = Perfil.objects.get(nomePerfil=request.user)
    is_amigo = amigo.amigo_set.filter(nomePerfil=perfil.nomePerfil).exists()
    return is_amigo
