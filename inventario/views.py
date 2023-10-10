from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
import os
from inventario.forms import PastaForm, FileForm
from inventario.models import Pasta, File

@login_required
def index(request):
    return render(request, 'inventario/index.html')


@login_required
def mapas(request):
    div = 'Mapas'
    user = request.user
    pastas = Pasta.objects.filter(owner=user, divisao='Mapas')
    
    if request.method == 'POST':
        form = PastaForm(request.POST)
        if form.is_valid():
            validation = form.save(commit=False)
            validation.owner = user
            validation.divisao = 'Mapas'
            validation.save()
            return redirect('mapas')
    else:
        form = PastaForm()

    return render(request, 'inventario/divisao.html', {'form': form, 'pastas': pastas, 'div': div})

@login_required
def criaturas(request):
    div = 'Criaturas'
    user = request.user
    pastas = Pasta.objects.filter(owner=user, divisao='Criaturas')
    
    if request.method == 'POST':
        form = PastaForm(request.POST)
        if form.is_valid():
            validation = form.save(commit=False)
            validation.owner = user
            validation.divisao = 'Criaturas'
            validation.save()
            return redirect('criaturas')
    else:
        form = PastaForm()

    return render(request, 'inventario/divisao.html', {'form': form, 'pastas': pastas, 'div': div})

@login_required
def documentos(request):
    div = 'Documentos'
    user = request.user
    pastas = Pasta.objects.filter(owner=user, divisao='Documentos')
    
    if request.method == 'POST':
        form = PastaForm(request.POST)
        if form.is_valid():
            validation = form.save(commit=False)
            validation.owner = user
            validation.divisao = 'Documentos'
            validation.save()
            return redirect('documentos')
    else:
        form = PastaForm()

    return render(request, 'inventario/divisao.html', {'form': form, 'pastas': pastas, 'div': div})

@login_required
def imagens(request):
    div = 'Imagens'
    user = request.user
    pastas = Pasta.objects.filter(owner=user, divisao='Imagens')
    
    if request.method == 'POST':
        form = PastaForm(request.POST)
        if form.is_valid():
            validation = form.save(commit=False)
            validation.owner = user
            validation.divisao = 'Imagens'
            validation.save()
            return redirect('imagens')
    else:
        form = PastaForm()

    return render(request, 'inventario/divisao.html', {'form': form, 'pastas': pastas, 'div': div})

@login_required
def musicas(request):
    div = 'Musicas'
    user = request.user
    pastas = Pasta.objects.filter(owner=user, divisao='Musicas')
    
    if request.method == 'POST':
        form = PastaForm(request.POST)
        if form.is_valid():
            validation = form.save(commit=False)
            validation.owner = user
            validation.divisao = 'Musicas'
            validation.save()
            return redirect('musicas')
    else:
        form = PastaForm()

    return render(request, 'inventario/divisao.html', {'form': form, 'pastas': pastas, 'div': div})


@login_required
def visualizar_pasta(request, div, pasta):
    user = request.user
    pastas = Pasta.objects.get(nome=pasta, owner=user)
    files = File.objects.filter(owner=user, pasta=pastas.id)

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            files = form.cleaned_data["file"]
            for f in files:
                arquivo = File(file=f, owner=user, pasta=pastas)
                arquivo.save()
            return redirect('visualizar_pasta', pasta)
    else:
        form = FileForm()

    return render(request, 'inventario/visualizar_pasta.html', {'files': files, 'form': form})

@login_required
def deletar(request, id):
    
     
    delete = get_object_or_404(Pasta, id=id)
    divisao = delete.divisao
    
    delete.delete()
    return redirect(divisao.lower())
