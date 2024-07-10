from django.shortcuts import render, get_object_or_404
from .models import Map, Token
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def enter_campaign(request, campaign_id):
    maps = Map.objects.filter(campanha_id=campaign_id)
    return render(request, 'tabletop/campaign.html', {'maps': maps, 'campaign_id': campaign_id})

def load_map(request, map_id):
    current_map = get_object_or_404(Map, id=map_id)
    tokens = Token.objects.filter(map=current_map)
    return render(request, 'tabletop/map.html', {'map': current_map, 'tokens': tokens})

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
