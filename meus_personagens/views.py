from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
import os
from django.contrib.auth.decorators import login_required
from django.db.models import Q


from home.models import Perfil
from tabletop.models import CallOfCthulhuCampanha, DnDCampanha, OrdemParanormalCampanha, TormentaCampanha
from .forms import DnDForm, OrdemParanormalForm, TormentaForm, CallOfCthulhuForm
from .models import DnD, OrdemParanormal, Tormenta, CallOfCthulhu

@login_required
def edit_dnd(request, id):
    personagem = get_object_or_404(DnD, pk=id)
    perfil = Perfil.objects.get(nomePerfil=request.user)
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

    return render(request, 'meus_personagens/editCharacter/edit_char_dnd.html', {'dnd': form, 'personagem': personagem, "fotoConta": perfil.fotoConta})

@login_required
def edit_ordem(request, id):
    personagem = get_object_or_404(OrdemParanormal, pk=id)
    perfil = Perfil.objects.get(nomePerfil=request.user)
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

    return render(request, 'meus_personagens/editCharacter/edit_char_ordem.html', {'ordem': form, 'personagem': personagem, "fotoConta": perfil.fotoConta})

@login_required
def edit_tormenta20(request, id):
    personagem = get_object_or_404(Tormenta, pk=id)
    perfil = Perfil.objects.get(nomePerfil=request.user)
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

    return render(request, 'meus_personagens/editCharacter/edit_char_tormenta20.html', {'tormenta': form, 'personagem': personagem, "fotoConta": perfil.fotoConta})

@login_required
def edit_coc1920(request, id):
    personagem = get_object_or_404(CallOfCthulhu, pk=id)
    perfil = Perfil.objects.get(nomePerfil=request.user)
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

    return render(request, 'meus_personagens/editCharacter/edit_char_coc1920.html', {'coc7e': form, 'personagem': personagem, "fotoConta": perfil.fotoConta})

@login_required
def deletarChar(request, rpg, id):
    user = request.user

    try:
        #Delete DND
        if rpg == 'dungeons&dragons':
            personagem = get_object_or_404(DnD, pk=id)
            if user == personagem.nomePerfil or user.is_staff:
                if personagem.foto:
                    os.remove(os.path.join('media', personagem.foto.name))
                personagem.delete()
                return redirect('meus_personagens')
            else:
                return redirect('meus_personagens')

        #Delete Ordem Paranormal
        if rpg == 'ordemparanormal':
            personagem = get_object_or_404(OrdemParanormal, pk=id)
            if user == personagem.nomePerfil or user.is_staff:
                if personagem.foto:
                    os.remove(os.path.join('media', personagem.foto.name))
                personagem.delete()
                return redirect('meus_personagens')
            else:
                return redirect('meus_personagens')

        #Delete Tormenta20
        if rpg == 'tormenta20':
            personagem = get_object_or_404(Tormenta, pk=id)
            if user == personagem.nomePerfil or user.is_staff:
                if personagem.foto:
                    os.remove(os.path.join('media', personagem.foto.name))
                personagem.delete()
                return redirect('meus_personagens')
            else:
                return redirect('meus_personagens')

        #Delete Tormenta20
        if rpg == 'callofcthulhu':
            personagem = get_object_or_404(CallOfCthulhu, pk=id)
            if user == personagem.nomePerfil or user.is_staff:
                if personagem.foto:
                    os.remove(os.path.join('media', personagem.foto.name))
                personagem.delete()
                return redirect('meus_personagens')
            else:
                return redirect('meus_personagens')
    except Exception as e:
        raise Http404(e)



@login_required
def index(request):
    user = request.user
    sistema_busca = request.GET.get('q')

    # Filtrar personagens por modelo, aplicando o sistema de busca se necessário
    dnd = DnD.objects.filter(nomePerfil=user)
    tormenta = Tormenta.objects.filter(nomePerfil=user)
    call_of_cthulhu = CallOfCthulhu.objects.filter(nomePerfil=user)
    ordem_paranormal = OrdemParanormal.objects.filter(nomePerfil=user)

    if sistema_busca:
        # Ajuste para busca no campo correto do modelo referenciado
        dnd = dnd.filter(nomePerfil__username__icontains=sistema_busca)
        tormenta = tormenta.filter(nomePerfil__username__icontains=sistema_busca)
        call_of_cthulhu = call_of_cthulhu.filter(nomePerfil__username__icontains=sistema_busca)
        ordem_paranormal = ordem_paranormal.filter(nomePerfil__username__icontains=sistema_busca)

    # Excluir personagens que já estão em campanhas
    ids_campanha_T = TormentaCampanha.objects.values_list('pk', flat=True)
    ids_campanha_D = DnDCampanha.objects.values_list('pk', flat=True)
    ids_campanha_O = OrdemParanormalCampanha.objects.values_list('pk', flat=True)
    ids_campanha_C = CallOfCthulhuCampanha.objects.values_list('pk', flat=True)

    dnd = dnd.exclude(id__in=ids_campanha_D)
    ordem_paranormal = ordem_paranormal.exclude(id__in=ids_campanha_O)
    tormenta = tormenta.exclude(id__in=ids_campanha_T)
    call_of_cthulhu = call_of_cthulhu.exclude(id__in=ids_campanha_C)

    # Combinar todos os personagens para exibição na interface
    personagens_filtro = list(dnd) + list(tormenta) + list(call_of_cthulhu) + list(ordem_paranormal)

    perfil = Perfil.objects.get(nomePerfil=user)

    return render(request, 'meus_personagens/index.html', {
        'personagens_filtro': personagens_filtro,
        'dnd': dnd,
        'ordem': ordem_paranormal,
        'tormenta20': tormenta,
        'coc': call_of_cthulhu,
        'fotoConta': perfil.fotoConta,
    })




@login_required
def criacao_char(request):
    perfil = Perfil.objects.get(nomePerfil=request.user)

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


    return render(request, 'meus_personagens/criacao_char.html', {'dnd': formDnD, 'ordem': formOrdem, 'tormenta': formTormenta, 'coc7e': formCoC, 'fotoConta': perfil.fotoConta })
