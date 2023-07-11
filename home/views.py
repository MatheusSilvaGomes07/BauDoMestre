from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Campanha
from .forms import CampanhaForm

def home(request):
    return render(request, 'principal/home.html')

def mural(request):
    campanhas = Campanha.objects.all()
    return render(request, 'principal/mural.html', {'campanhas': campanhas})

@login_required
def criarCampanhas(request):
    if request.method == 'POST':
        form = CampanhaForm(request.POST, request.FILES)
        if form.is_valid():
            campanha = form.save(commit=False)
            campanha.nomeMestre = request.user
            campanha.save()
            return redirect('mural')
    else:
        form = CampanhaForm()
    
    return render(request, 'principal/criarMesas.html', {'form': form}) 

@login_required
def teste(request):
    return render(request, 'principal/teste.html')

@login_required
def usuario(request):
    return render(request, 'principal/user.html')
