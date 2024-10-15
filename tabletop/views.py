from django.shortcuts import redirect, render, get_object_or_404
from .models import CallOfCthulhuCampanha, DnDCampanha, Map, OrdemParanormalCampanha, Token, PastaCriaturas, TormentaCampanha
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .membro_decorator import user_in_group
from .mestre_decorator import is_mestre
from .forms import MapForm, TokenForm, CampanhaDnDForm, CampanhaOrdemParanormalForm, CampanhaCallOfCthulhuCForm, CampanhaTormentaForm, PastaCriaturasForm
from home.models import Campanha
from django.contrib.contenttypes.models import ContentType

@user_in_group
#SE NÃO FOR MEMBRO DA CAMPANHA, É REDIRECIONADO PARA O BUSCAR MESA
@is_mestre
def enter_campaign(request, campaign_id, is_mestre):
    maps = Map.objects.filter(campanha_id=campaign_id)
    campanha = Campanha.objects.get(id=campaign_id)
    pastaCriaturas = PastaCriaturas.objects.filter(campanha_id=campaign_id)
    
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
        personagemForm = CampanhaDnDForm()
    elif sistemaCampanha == "Call of Cthulu":
        personagemForm = CampanhaCallOfCthulhuCForm()
    elif sistemaCampanha == "Ordem Paranormal":
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
    elif sistema == 'Call of Cthulu':
        personagem_model = CallOfCthulhuCampanha
    else:
        print('Deu ruim')
    
    content_type = ContentType.objects.get_for_model(personagem_model)
    personagem = personagem_model.objects.get(id=personagem_id)

    token = Token.objects.create(
        content_type=content_type,
        object_id=personagem.id,
        map=mapa,
        position_x = 372,
        position_y = -487,
        image = personagem.foto
    )

    return redirect('load_map', map_id)