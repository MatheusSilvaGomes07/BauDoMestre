from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import DnDForm, OrdemParanormalForm
from .models import DnD, OrdemParanormal
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    dnd = DnD.objects.all()
    ordem = OrdemParanormal.objects.all()

    todos_personagens = list(dnd) + list(ordem)

    return render(request, 'meus_personagens/index.html', {
        'todos_personagens': todos_personagens
    })

@login_required
def criacao_char(request):
    if request.method == 'POST':
        formDnD = DnDForm(request.POST)
        if formDnD.is_valid():
            dnd = formDnD.save(commit=False)
            dnd.nomePerfil = request.user
            dnd.save()
            return redirect('meus_personagens')  # Redirecione para a página de listagem de produtos
    else:
        formDnD = DnDForm()
    
    if request.method == 'POST':
        formOrdem = OrdemParanormalForm(request.POST)
        if formOrdem.is_valid():
            ordem = formOrdem.save(commit=False)
            ordem.nomePerfil = request.user
            ordem.save()
            return redirect('meus_personagens')
    else:
        formOrdem = OrdemParanormalForm()

    return render(request, 'meus_personagens/criacao_char.html', {'dnd': formDnD, 'ordem': formOrdem})

def detail_charDnD(request, id):
    personagem = get_object_or_404(DnD, pk=id)

    return render(request, 'meus_personagens/detail_char.html', {'personagem': personagem})

def detail_charOrdemParanormal(request, id):
    personagem = get_object_or_404(OrdemParanormal, pk=id)

    return render(request, 'meus_personagens/detail_char.html', {'personagem': personagem})
