from django.shortcuts import render, redirect
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
    campanhas = Campanha.objects.all()

    if sistema_busca:
        campanhas = campanhas.filter(
            Q(nomeCampanha__icontains=sistema_busca)
        )
    return render(request, 'principal/muralLogado.html', {'campanhas': campanhas})

@login_required
def criarCampanhas(request):
    if request.method == 'POST':
        form = CampanhaForm(request.POST, request.FILES)
        if form.is_valid():
            campanha = form.save(commit=False)
            campanha.nomeMestre = request.user
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
    perfil, created = Perfil.objects.update_or_create(nomePerfil=request.user, defaults={
        'descricao': request.POST.get('descricao', 'Indefinido'),
        'tipo_sessao': request.POST.get('tipo_sessao', 'Indefinido'),
        'tipo_player': request.POST.get('tipo_player', 'Indefinido'),
        'sistema_rpg': request.POST.get('sistema_rpg', 'Indefinido')
    })

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

