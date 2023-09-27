from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import DnDForm, OrdemParanormalForm, TormentaForm, CallOfCthulhuForm
from .models import DnD, OrdemParanormal, Tormenta, CallOfCthulhu
from django.contrib.auth.decorators import login_required
import os

@login_required
def edit_dnd(request, id):
    personagem = get_object_or_404(DnD, pk=id)
    user = request.user
    foto_antiga = personagem.foto.name


    if user == personagem.nomePerfil or user.is_staff:
        if request.method == "POST":
            form = DnDForm(request.POST, request.FILES, instance=personagem)
            if form.is_valid():
                if personagem.foto:
                    

                    caminho_arquivo_antigo = os.path.join('media', foto_antiga)
                    if foto_antiga != personagem.foto:
                        os.remove(caminho_arquivo_antigo)
                form.save()
                return redirect('meus_personagens')
        else:
            form = DnDForm(instance=personagem)
    else:
         return redirect('meus_personagens')
    
    return render(request, 'meus_personagens/editCharacter/edit_char_dnd.html', {'dnd': form, 'personagem': personagem})

@login_required
def edit_ordem(request, id):
    personagem = get_object_or_404(OrdemParanormal, pk=id)
    user = request.user
    foto_antiga = personagem.foto.name

    if user == personagem.nomePerfil or user.is_staff:
        if request.method == "POST":
            form = OrdemParanormalForm(request.POST, request.FILES, instance=personagem)
            if form.is_valid():
                if personagem.foto:
                    

                    caminho_arquivo_antigo = os.path.join('media', foto_antiga)

                    if foto_antiga != personagem.foto:
                        os.remove(caminho_arquivo_antigo)
                form.save()
                return redirect('meus_personagens')
        else:
            form = OrdemParanormalForm(instance=personagem)
    else:
         return redirect('meus_personagens')
    
    return render(request, 'meus_personagens/editCharacter/edit_char_ordem.html', {'ordem': form, 'personagem': personagem})

@login_required
def edit_tormenta20(request, id):
    personagem = get_object_or_404(Tormenta, pk=id)
    user = request.user
    foto_antiga = personagem.foto.name

    if user == personagem.nomePerfil or user.is_staff:
        if request.method == "POST":
            form = TormentaForm(request.POST, request.FILES, instance=personagem)
            if form.is_valid():
                if personagem.foto:
                    

                    caminho_arquivo_antigo = os.path.join('media', foto_antiga)

                    if foto_antiga != personagem.foto:
                        os.remove(caminho_arquivo_antigo)
                form.save()
                return redirect('meus_personagens')
        else:
            form = TormentaForm(instance=personagem)
    else:
         return redirect('meus_personagens')
    
    return render(request, 'meus_personagens/editCharacter/edit_char_tormenta20.html', {'tormenta': form, 'personagem': personagem})

@login_required
def edit_coc1920(request, id):
    personagem = get_object_or_404(CallOfCthulhu, pk=id)
    user = request.user
    foto_antiga = personagem.foto.name

    if user == personagem.nomePerfil or user.is_staff:
        if request.method == "POST":
            form = CallOfCthulhuForm(request.POST, request.FILES, instance=personagem)
            if form.is_valid():
                if personagem.foto:
                    

                    caminho_arquivo_antigo = os.path.join('media', foto_antiga)

                    if foto_antiga != personagem.foto:
                        os.remove(caminho_arquivo_antigo)
                form.save()
                return redirect('meus_personagens')
        else:
            form = CallOfCthulhuForm(instance=personagem)
    else:
         return redirect('meus_personagens')
    
    return render(request, 'meus_personagens/editCharacter/edit_char_coc1920.html', {'coc7e': form, 'personagem': personagem})

            
@login_required
def index(request):
    user = request.user

    dnd = DnD.objects.filter(nomePerfil=user)
    ordem = OrdemParanormal.objects.filter(nomePerfil=user)
    tormenta20 = Tormenta.objects.filter(nomePerfil=user)
    coc = CallOfCthulhu.objects.filter(nomePerfil=user)

    return render(request, 'meus_personagens/index.html', { 'dnd': dnd, 'ordem': ordem, 'tormenta20': tormenta20, 'coc': coc })

@login_required
def criacao_char(request):
    if request.method == 'POST':
        formDnD = DnDForm(request.POST, request.FILES)
        if formDnD.is_valid():
            dnd = formDnD.save(commit=False)
            dnd.nomePerfil = request.user
            dnd.save()
            return redirect('meus_personagens')
    else:
        formDnD = DnDForm()
    
    if request.method == 'POST':
        formOrdem = OrdemParanormalForm(request.POST, request.FILES)
        if formOrdem.is_valid():
            ordem = formOrdem.save(commit=False)
            ordem.nomePerfil = request.user
            ordem.save()
            return redirect('meus_personagens')
    else:
        formOrdem = OrdemParanormalForm()

    if request.method == 'POST':
        formTormenta = TormentaForm(request.POST, request.FILES)
        if formTormenta.is_valid():
            tormenta = formTormenta.save(commit=False)
            tormenta.nomePerfil = request.user
            tormenta.save()
            return redirect('meus_personagens')
    else:
        formTormenta = TormentaForm()

    if request.method == 'POST':
        formCoC = CallOfCthulhuForm(request.POST, request.FILES)
        if formCoC.is_valid():
            CoC =  formCoC.save(commit=False)
            CoC.nomePerfil = request.user
            CoC.save()
            return redirect('meus_personagens')
    else:
         formCoC = CallOfCthulhuForm()
    

    return render(request, 'meus_personagens/criacao_char.html', {'dnd': formDnD, 'ordem': formOrdem, 'tormenta': formTormenta, 'coc7e': formCoC })

@login_required
def detail_charDnD(request, id):
    personagem = get_object_or_404(DnD, pk=id)
    user = request.user

    if user == personagem.nomePerfil or user.is_staff:
        return render(request, 'meus_personagens/detailCharacter/detail_char_dnd.html', {'personagem': personagem})
    else:
         return redirect('meus_personagens')
    
@login_required
def detail_charOrdemParanormal(request, id):
    personagem = get_object_or_404(OrdemParanormal, pk=id)
    user = request.user

    if user == personagem.nomePerfil or user.is_staff:
        return render(request, 'meus_personagens/detailCharacter/detail_char_ordem.html', {'personagem': personagem})
    else:
         return redirect('meus_personagens')
    
@login_required
def detail_charTormenta(request, id):
    personagem = get_object_or_404(Tormenta, pk=id)
    user = request.user

    if user == personagem.nomePerfil or user.is_staff:
        return render(request, 'meus_personagens/detailCharacter/detail_char_tormenta.html', {'personagem': personagem})
    else:
         return redirect('meus_personagens')

@login_required
def detail_charCoC(request, id):
    personagem = get_object_or_404(CallOfCthulhu, pk=id)
    user = request.user

    if user == personagem.nomePerfil or user.is_staff:
        return render(request, 'meus_personagens/detailCharacter/detail_char_coc.html', {'personagem': personagem})
    else:
         return redirect('meus_personagens')
