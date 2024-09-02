from django.shortcuts import redirect, render, get_object_or_404
from .models import Map, Token
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .membro_decorator import user_in_group
from .mestre_decorator import is_mestre
from .forms import MapForm
from home.models import Campanha

@user_in_group
#SE NÃO FOR MEMBRO DA CAMPANHA, É REDIRECIONADO PARA O BUSCAR MESA
@is_mestre
def enter_campaign(request, campaign_id, is_mestre):
    maps = Map.objects.filter(campanha_id=campaign_id)
    form = MapForm()
    if is_mestre:
        if request.method == "POST":
            form = MapForm(request.POST, request.FILES)
            if form.is_valid():
                mapa = form.save(commit=False)
                mapa.campanha_id = get_object_or_404(Campanha, id=campaign_id)
                mapa.save()
                return redirect('enter_campaign', campaign_id)
        return render(request, 'tabletop/campaign.html', {'maps': maps, 'campaign_id': campaign_id, 'is_mestre': is_mestre, 'form': form})
    return render(request, 'tabletop/campaign.html', {'maps': maps, 'campaign_id': campaign_id, 'is_mestre': is_mestre})

@login_required
def load_map(request, map_id):
    current_map = get_object_or_404(Map, id=map_id)
    tokens = Token.objects.filter(map=current_map)
    return render(request, 'tabletop/map.html', {'map': current_map, 'tokens': tokens})


@login_required 
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
        