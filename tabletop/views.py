import os
import random
from django.shortcuts import redirect, render, get_object_or_404
from meus_personagens.forms import CallOfCthulhuForm, DnDForm, OrdemParanormalForm, TormentaForm
from .models import CallOfCthulhuCampanha, DnDCampanha, Map, OrdemParanormalCampanha, Token, PastaCriaturas, TormentaCampanha
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .membro_decorator import user_in_group
from .mestre_decorator import is_mestre
from .forms import MapForm, TokenForm, CampanhaDnDForm, CampanhaOrdemParanormalForm, CampanhaCallOfCthulhuCForm, CampanhaTormentaForm, PastaCriaturasForm
from home.models import Campanha
from django.contrib.contenttypes.models import ContentType
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@user_in_group
#SE NÃO FOR MEMBRO DA CAMPANHA, É REDIRECIONADO PARA O BUSCAR MESA
@is_mestre
def enter_campaign(request, campaign_id, is_mestre):
    maps = Map.objects.filter(campanha_id=campaign_id)
    campanha = Campanha.objects.get(id=campaign_id)
    pastaCriaturas = PastaCriaturas.objects.filter(campanha_id=campaign_id)
    detalhePersonagem = None
    # Dicionário para armazenar personagens por pasta
    pasta_personagens = {}

    # Itera sobre cada pasta e coleta todos os personagens associados
    for pasta in pastaCriaturas:
        # Verifica o sistema de RPG associado à campanha
        sistema_rpg = campanha.sistemaCampanha

        # Filtra personagens apenas do sistema associado à campanha
        if sistema_rpg == 'Dungeons & Dragons':
            personagens = DnDCampanha.objects.filter(pasta=pasta)
            detalhePersonagem = 'detail_char_ordem'
        elif sistema_rpg == 'Ordem Paranormal':
            personagens = OrdemParanormalCampanha.objects.filter(pasta=pasta)
            detalhePersonagem = 'detail_char_tormenta'
        elif sistema_rpg == 'Tormenta20':
            personagens = TormentaCampanha.objects.filter(pasta=pasta)
            detalhePersonagem = 'detail_char_tormenta'
        elif sistema_rpg == 'Call of Cthulu':
            personagens = CallOfCthulhuCampanha.objects.filter(pasta=pasta)
            detalhePersonagem = 'detail_char_coc'
        else:
            personagens = []

        # Armazena os personagens em um dicionário, com a pasta como chave
        pasta_personagens[pasta] = personagens

    tokenForm = TokenForm()
    if is_mestre:
        form = MapForm()
        pastaCritaturasForm = PastaCriaturasForm()
        if request.method == "POST":
            form = MapForm(request.POST, request.FILES)
            if form.is_valid():
                mapa = form.save(commit=False)
                mapa.campanha_id = get_object_or_404(Campanha, id=campaign_id)
                mapa.save()
                return redirect('enter_campaign', campaign_id)
        return render(request, 'tabletop/campaign.html', {
            'maps': maps,
            'campaign_id': campaign_id,
            'is_mestre': is_mestre,
            'form': form,
            'tokenForm': tokenForm,
            'pastaCriaturasForm' : pastaCritaturasForm,
            'pasta_personagens': pasta_personagens,
            'detalhePersonagem' : detalhePersonagem
        })

    return render(request, 'tabletop/campaign.html', {
        'maps': maps,
        'campaign_id': campaign_id,
        'pasta_personagens': pasta_personagens,
        'is_mestre': is_mestre,
        'detalhePersonagem' : detalhePersonagem
    })

@user_in_group
def load_map(request, map_id):
    current_map = get_object_or_404(Map, id=map_id)
    tokens = Token.objects.filter(map=current_map)
    return render(request, 'tabletop/map.html', {'map': current_map, 'tokens': tokens})


@user_in_group
@csrf_exempt
def move_token(request, token_id):
    if request.method == 'POST':
        position_x = request.POST.get('position_x')
        position_y = request.POST.get('position_y')

        token = Token.objects.get(id=token_id)
        token.position_x = position_x
        token.position_y = position_y
        token.save()

        return JsonResponse({'status': 'success'})


@is_mestre
def deletar_mapa(request, campaign_id, map_id, is_mestre):
    if is_mestre:
        mapa = get_object_or_404(Map, id=map_id)

        mapa.delete()

    return redirect('enter_campaign', campaign_id)

@is_mestre
def criarPastaCriaturas(request, campaign_id, is_mestre):
    if is_mestre:
        if request.method == "POST":
            form = PastaCriaturasForm(request.POST)
            if form.is_valid():
                pasta = form.save(commit=False)
                pasta.campanha = get_object_or_404(Campanha, pk = campaign_id)
                pasta.save()
    return redirect ('enter_campaign', campaign_id)
@is_mestre
def deletarPastaCriaturas(request, campaign_id, pasta_id, is_mestre):
    if is_mestre:

        pasta = PastaCriaturas(id=pasta_id)

        pasta.delete()

    return redirect('enter_campaign', campaign_id)

@user_in_group
def criar_personagem(request, campaign_id, pasta_id):
    campanha = get_object_or_404(Campanha, id=campaign_id)
    pasta = get_object_or_404(PastaCriaturas, id = pasta_id)
    sistemaCampanha = campanha.sistemaCampanha

    if sistemaCampanha == "Tormenta20":
        if request.method == 'POST':
            personagemForm = CampanhaTormentaForm(request.POST, request.FILES)
            if personagemForm.is_valid():
                personagem = personagemForm.save(commit=False)
                personagem.nomePerfil = request.user
                personagem.campanha_id = campanha
                personagem.pasta = pasta
                personagem.save()
                return redirect('enter_campaign', campaign_id=campaign_id)
        else:
            personagemForm = CampanhaTormentaForm()

    elif sistemaCampanha == "Dungeons & Dragons":
        personagemForm = CampanhaDnDForm(request.POST, request.FILES)
        if personagemForm.is_valid():
                personagem = personagemForm.save(commit=False)
                personagem.nomePerfil = request.user
                personagem.campanha_id = campanha
                personagem.pasta = pasta
                personagem.save()
                return redirect('enter_campaign', campaign_id=campaign_id)
        else:
            personagemForm =CampanhaDnDForm()
    elif sistemaCampanha == "Call of Cthulu":
        personagemForm = CampanhaCallOfCthulhuCForm(request.POST, request.FILES)
        if personagemForm.is_valid():
                personagem = personagemForm.save(commit=False)
                personagem.nomePerfil = request.user
                personagem.campanha_id = campanha
                personagem.pasta = pasta
                personagem.save()
                return redirect('enter_campaign', campaign_id=campaign_id)
        else:
            personagemForm = CampanhaCallOfCthulhuCForm()
    elif sistemaCampanha == "Ordem Paranormal":
        personagemForm = CampanhaOrdemParanormalForm(request.POST, request.FILES)
        if personagemForm.is_valid():
                personagem = personagemForm.save(commit=False)
                personagem.nomePerfil = request.user
                personagem.campanha_id = campanha
                personagem.pasta = pasta
                personagem.save()
                return redirect('enter_campaign', campaign_id=campaign_id)
        else:
            personagemForm = CampanhaOrdemParanormalForm()

    return render(request, 'tabletop/criarPersonagem.html', {'personagemForm': personagemForm})

def place_token(request, map_id, personagem_id):
    mapa = get_object_or_404(Map, id=map_id)
    sistema = mapa.campanha_id.sistemaCampanha

    if sistema == 'Dungeons & Dragons':
        personagem_model = DnDCampanha
    elif sistema == 'Ordem Paranormal':
        personagem_model = OrdemParanormalCampanha
    elif sistema == 'Tormenta20':
        personagem_model = TormentaCampanha
    elif sistema == 'Call of Cthulhu':
        personagem_model = CallOfCthulhuCampanha
    else:
        return JsonResponse({'error': 'Sistema de RPG desconhecido'}, status=400)

    content_type = ContentType.objects.get_for_model(personagem_model)
    personagem = personagem_model.objects.get(id=personagem_id)

    token = Token.objects.create(
        content_type=content_type,
        object_id=personagem.id,
        map=mapa,
        position_x=600,           # Tamanho pré-definido dependendo do tamanho do mapa
        position_y=415,           # Tamanho pré-definido dependendo do tamanho do mapa
        image=personagem.foto
    )

    # Enviar a mensagem pelo WebSocket
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'campaign_{mapa.campanha_id.id}',
        {
            'type': 'place_token',
            'token_id': token.id,
            'position_x': token.position_x,
            'position_y': token.position_y,
            'image': token.image.url  # Supondo que você deseja enviar a URL da imagem
        }
    )

    return JsonResponse({'status': 'success', 'token_id': token.id})

def deletar_personagem_campanha (request, campaign_id, personagem_id):
    campanha = get_object_or_404(Campanha, id=campaign_id)
    sistema = campanha.sistemaCampanha
    user = request.user

    if sistema == 'Dungeons & Dragons':
        personagem_model = DnDCampanha
    elif sistema == 'Ordem Paranormal':
        personagem_model = OrdemParanormalCampanha
    elif sistema == 'Tormenta20':
        personagem_model = TormentaCampanha
    elif sistema == 'Call of Cthulhu':
        personagem_model = CallOfCthulhuCampanha
    else:
        return JsonResponse({'error': 'Sistema de RPG desconhecido'}, status=400)

    personagem = get_object_or_404(personagem_model, id=personagem_id)
    if user == personagem.nomePerfil or user.is_staff:
        if personagem.foto:
            os.remove(os.path.join('media', personagem.foto.name))
            personagem.delete()
            return redirect('enter_campaign', campaign_id)
        else:
            return redirect('meus_personagens', campaign_id)

def editar_personagem_campanha(request, campaign_id, personagem_id):
    campanha = get_object_or_404(Campanha, id=campaign_id)
    sistema = campanha.sistemaCampanha
    user = request.user

    if sistema == 'Dungeons & Dragons':
        personagem_model = DnDCampanha
        personagem_form = DnDForm
    elif sistema == 'Ordem Paranormal':
        personagem_model = OrdemParanormalCampanha
        personagem_form = OrdemParanormalForm
    elif sistema == 'Tormenta20':
        personagem_model = TormentaCampanha
        personagem_form = TormentaForm
    elif sistema == 'Call of Cthulhu':
        personagem_model = CallOfCthulhuCampanha
        personagem_form = CallOfCthulhuForm
    else:
        return JsonResponse({'error': 'Sistema de RPG desconhecido'}, status=400)

    personagem = get_object_or_404(personagem_model, id=personagem_id)
    foto_antiga = personagem.foto.name

    if user == personagem.nomePerfil or user.is_staff:
        if request.method == "POST":
            form = personagem_form(request.POST, request.FILES, instance=personagem)
            if form.is_valid():
                if personagem.foto:

                    caminho_arquivo_antigo = os.path.join('media', foto_antiga)

                    if foto_antiga != personagem.foto:
                        os.remove(caminho_arquivo_antigo)
                form.save()
                return redirect('meus_personagens')
        else:
            form = personagem_form(instance=personagem)
    else:
         return redirect('meus_personagens')

    return render(request, 'meus_personagens/editCharacter/edit_char_ordem.html', {'ordem': form, 'personagem': personagem})

def editar_personagem_campanha(request, campaign_id, personagem_id):
    campanha = get_object_or_404(Campanha, id=campaign_id)
    sistema = campanha.sistemaCampanha
    user = request.user
    personagem = None
    template = ''
    form_name = ''

    if sistema == 'Dungeons & Dragons':
        personagem = get_object_or_404(DnDCampanha, id=personagem_id)
        personagem_form = DnDForm
        template = 'edit_char_dnd.html'
        form_name = 'dnd'
    elif sistema == 'Ordem Paranormal':
        personagem = get_object_or_404(OrdemParanormalCampanha, id=personagem_id)
        personagem_form = OrdemParanormalForm
        template = 'edit_char_ordem.html'
        form_name = 'ordem'
    elif sistema == 'Tormenta20':
        personagem = get_object_or_404(TormentaCampanha, id=personagem_id)
        personagem_form = TormentaForm
        template = 'edit_char_tormenta20.html'
        form_name = 'tormenta'
    elif sistema == 'Call of Cthulhu':
        personagem = get_object_or_404(CallOfCthulhuCampanha, id=personagem_id)
        personagem_form = CallOfCthulhuForm
        template = 'edit_char_coc1920.html'
        form_name = 'coc7e'
    else:
        return JsonResponse({'error': 'Sistema de RPG desconhecido'}, status=400)


    if user == personagem.nomePerfil or user.is_staff:
        foto_antiga = personagem.foto.name

        if request.method == "POST":
            form = personagem_form(request.POST, request.FILES, instance=personagem)
            if form.is_valid():
                if personagem.foto:
                    caminho_arquivo_antigo = os.path.join('media', foto_antiga)

                    if foto_antiga != personagem.foto:
                        os.remove(caminho_arquivo_antigo)
                form.save()
                print('Local 1')
                return redirect('enter_campaign', campaign_id)
        else:
            form = personagem_form(instance=personagem)
    else:
        print('Local 2')
        return redirect('enter_campaign', campaign_id)

    return render(request, 'meus_personagens/editCharacter/' + template, {form_name: form, 'personagem': personagem})

@csrf_exempt
@user_in_group
def roll_dice(request, campaign_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        dice_type = int(request.POST.get('type'))
        modifier = int(request.POST.get('modifier'))

        total = 0
        rolls = []

        for _ in range(quantity):
            roll = random.randint(1, dice_type)
            rolls.append(roll)
            total += roll

        total += modifier

        result = {
            'rolls': rolls,
            'total': total
        }

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'campaign_{campaign_id}',
            {
                'type': 'roll_dice',
                'quantity': quantity,
                'dice_type': dice_type,
                'modifier': modifier,
                'result': result
            }
        )

        return JsonResponse({'status': 'success', 'result': result})
    return JsonResponse({'status': 'error'}, status=400)
