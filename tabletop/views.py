# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed, JsonResponse
from .models import Token, Map, Token
from .forms import TokenForm, MapForm, TokenForm
from django.views.decorators.csrf import csrf_exempt

# Função para criar um novo mapa
def create_map(request):
    if request.method == 'POST':
        form = MapForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create_map')
    else:
        form = MapForm()
    
    maps = Map.objects.all()
    return render(request, 'tabletop/create_map.html', {'form': form, 'maps': maps})

# Função para entrar em um mapa existente
def enter_map(request, map_id):
    map_instance = Map.objects.get(id=map_id)
    tokens = Token.objects.filter(map_id=map_id)
    return render(request, 'tabletop/enter_map.html', {'map': map_instance, 'tokens': tokens})

# Função para fazer upload de um token para um mapa específico
def upload_token(request):
    if request.method == 'POST':
        form = TokenForm(request.POST, request.FILES)
        if form.is_valid():
            token = form.save(commit=False)
            token.map_id = request.POST.get('map_id')  # Adiciona o ID do mapa ao token
            token.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Formulário inválido'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Método de requisição inválido'})

# Função para atualizar a posição de um token
@csrf_exempt
def update_token_position(request, map_id):
    if request.method == 'POST':
        token_id = request.POST.get('token_id')
        position_x = request.POST.get('position_x')
        position_y = request.POST.get('position_y')

        try:
            token = Token.objects.get(id=token_id)
            token.position_x = position_x
            token.position_y = position_y
            token.save()
            return JsonResponse({'status': 'success'})
        except Token.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Token not found'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

# Função para excluir todas as imagens
def delete_all_images(request):
    if request.method == 'POST':
        Token.objects.all().delete()
        return redirect('create_map')  # Redireciona de volta para a página de criação de mapa
    else:
        return HttpResponseNotAllowed(['POST'])
