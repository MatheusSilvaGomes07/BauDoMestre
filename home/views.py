from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'principal/home.html')

def login(request):
    return render(request, 'principal/login.html')

def cadastro(request):
    return render(request, 'principal/cadastro.html')

def mural(request):
    return render(request, 'principal/mural.html')

@login_required
def teste(request):
    return render(request, 'principal/teste.html')
