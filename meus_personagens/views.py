from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import DnDForm, OrdemParanormalForm, TormentaForm, CallOfCthulhuForm
from .models import DnD, OrdemParanormal, Tormenta, CallOfCthulhu
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    dnd = DnD.objects.all()
    ordem = OrdemParanormal.objects.all()
    tormenta20 = Tormenta.objects.all()
    coc = CallOfCthulhu.objects.all()

    todos_personagens = list(dnd) + list(ordem) + list(tormenta20) + list(coc)

    return render(request, 'meus_personagens/index.html', {'todos_personagens': todos_personagens})

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

    if request.method == 'POST':
        formTormenta = TormentaForm(request.POST)
        if formTormenta.is_valid():
            tormenta = formTormenta.save(commit=False)
            tormenta.nomePerfil = request.user
            tormenta.save()
            return redirect('meus_personagens')
    else:
        formTormenta = TormentaForm()

    if request.method == 'POST':
        formCoC = CallOfCthulhuForm(request.POST)
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

    return render(request, 'meus_personagens/detail_char.html', {'personagem': personagem})

@login_required
def detail_charOrdemParanormal(request, id):
    personagem = get_object_or_404(OrdemParanormal, pk=id)

    return render(request, 'meus_personagens/detail_char.html', {'personagem': personagem})
