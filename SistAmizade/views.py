from django.shortcuts import render, redirect
from .models import SolicitacaoAmizade, Amigo
from django.contrib.auth.models import User

def adicionar_amigo(request, user_id):
    amigo = User.objects.get(pk=user_id)
    
    solicitacao, _ = SolicitacaoAmizade.objects.get_or_create(de_usuario=request.user, para_usuario=amigo)
    
    return redirect('listar_amigos')

def remover_amigo(request, user_id):
    amigo = User.objects.get(pk=user_id)

    Amigo.objects.filter(usuario=request.user, amigo=amigo).delete()    
    Amigo.objects.filter(usuario=amigo, amigo=request.user).delete()

    return redirect('listar_amigos')


def listar_amigos(request):
    amigos = Amigo.objects.filter(usuario=request.user)
    return render(request, 'listar_amigos.html', {'amigos': amigos})


def enviar_solicitacao(request, user_id):
    para_usuario = User.objects.get(pk=user_id)
    solicitacao, criada = SolicitacaoAmizade.objects.get_or_create(de_usuario=request.user, para_usuario=para_usuario)

    if criada:
        return redirect('listar_amigos')
    else:
       
        return redirect('listar_amigos')

def listar_solicitacoes(request):
    solicitacoes_recebidas = SolicitacaoAmizade.objects.filter(para_usuario=request.user, aceita=False)
    return render(request, 'listar_solicitacoes.html', {'solicitacoes_recebidas': solicitacoes_recebidas})

def aceitar_solicitacao(request, solicitacao_id):
    solicitacao = SolicitacaoAmizade.objects.get(pk=solicitacao_id)
    solicitacao.aceita = True
    solicitacao.save()

    if not Amigo.objects.filter(usuario=solicitacao.de_usuario, amigo=solicitacao.para_usuario).exists():
        Amigo.objects.create(usuario=solicitacao.de_usuario, amigo=solicitacao.para_usuario)
    
    if not Amigo.objects.filter(usuario=solicitacao.para_usuario, amigo=solicitacao.de_usuario).exists():
        Amigo.objects.create(usuario=solicitacao.para_usuario, amigo=solicitacao.de_usuario)

    return redirect('listar_amigos')

def recusar_solicitacao(request, solicitacao_id):
    solicitacao = SolicitacaoAmizade.objects.get(pk=solicitacao_id)
    solicitacao.delete()
    return redirect('listar_amigos')
