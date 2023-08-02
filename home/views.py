from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Campanha, Perfil
from .forms import CampanhaForm, PerfilForm
from django.db.models import Q


def home(request):
    return render(request, 'principal/home.html')

def mural(request):
    campanhas = Campanha.objects.all()
    return render(request, 'principal/mural.html', {'campanhas': campanhas})

@login_required
def buscarmesa(request):
    sistema_busca = request.GET.get('q')
    sistema_filtro = request.GET.get('sistema')
    ambiente_filtro = request.GET.get('ambiente')
    genero_filtro = request.GET.get('genero')
    campanhas = Campanha.objects.all()

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

    return render(request, 'principal/muralLogado.html', {'campanhas': campanhas})


@login_required
def search_user(request):
    conta_busca = request.GET.get('q')
    users = []
    if conta_busca:
        users = Perfil.objects.filter(
            Q(nomePerfil__username__icontains=conta_busca)
        )
    return render(request, 'principal/buscaUser.html', {'users': users, 'busca_realizada': bool(conta_busca)})


@login_required
def exibir_perfil(request, perfil_slug):
    perfil = get_object_or_404(Perfil, slug=perfil_slug)
    return render(request, 'principal/exibir_perfil.html', {'perfil': perfil})

@login_required
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


@login_required
def teste(request):
    return render(request, 'principal/teste.html')

@login_required
def usuario(request):
    perfil = Perfil.objects.get(nomePerfil=request.user)
    return render(request, 'principal/user.html', {'perfil': perfil})

@login_required
def editarconta(request):
    perfil, created = Perfil.objects.update_or_create(nomePerfil=request.user)

    if request.method == 'POST':
        formPerfil = PerfilForm(request.POST, request.FILES, instance=perfil)
        if formPerfil.is_valid():
            if 'fotoConta' in request.FILES:
                perfil.fotoConta = request.FILES['fotoConta']
            formPerfil.save()
            return redirect('usuario')
    else:
        formPerfil = PerfilForm(instance=perfil)

    return render(request, 'principal/editarPerfil.html', {'formPerfil': formPerfil})

