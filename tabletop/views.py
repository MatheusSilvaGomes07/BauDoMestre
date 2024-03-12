# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed, JsonResponse
from .models import Object
from .forms import ObjectForm
from django.views.decorators.csrf import csrf_exempt

def tabletop_view(request):
    if request.method == 'POST':
        form = ObjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tabletop_view')  # Redirecionamento após o envio bem-sucedido
    else:
        form = ObjectForm()
    
    objects = Object.objects.all()
    return render(request, 'tabletop/tabletop.html', {'objects': objects, 'form': form})

@csrf_exempt
def update_object_position(request):
    if request.method == 'POST':
        # Receba os dados enviados pela solicitação AJAX
        object_id = request.POST.get('object_id')
        position_x = request.POST.get('position_x')
        position_y = request.POST.get('position_y')

        try:
            # Obtenha o objeto correspondente do banco de dados
            obj = Object.objects.get(id=object_id)
            # Atualize as coordenadas do objeto
            obj.position_x = position_x
            obj.position_y = position_y
            obj.save()
            return JsonResponse({'status': 'success'})
        except Object.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Object not found'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    

def delete_all_images(request):
    if request.method == 'POST':
        # Exclua todas as imagens do banco de dados
        Object.objects.all().delete()
        # Redirecione de volta para a página inicial
        return redirect('tabletop_view')
    else:
        # Se o método não for POST, retorne uma resposta de método não permitido
        return HttpResponseNotAllowed(['POST'])