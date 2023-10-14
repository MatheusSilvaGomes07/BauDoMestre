from django.shortcuts import render, redirect
from .models import SolicitacaoAmizade
from django.contrib.auth.models import User

def adicionar_amigo(request, user_id):
    amigo = User.objects.get(pk=user_id)
    SolicitacaoAmizade.objects.create(de_usuario=request.user, para_usuario=amigo)
    return redirect('listar_amigos')

def remover_amigo(request, user_id):
    amigo = User.objects.get(pk=user_id)
    SolicitacaoAmizade.objects.filter(de_usuario=request.user, para_usuario=amigo).delete()
    return redirect('listar_amigos')

def listar_amigos(request):
    amigos = SolicitacaoAmizade.objects.filter(de_usuario=request.user)
    return render(request, 'listar_amigos.html', {'amigos': amigos})


def enviar_solicitacao(request, user_id):
    para_usuario = User.objects.get(pk=user_id)
    SolicitacaoAmizade.objects.get_or_create(de_usuario=request.user, para_usuario=para_usuario)
    return redirect('listar_amigos')

def listar_solicitacoes(request):
    solicitacoes_recebidas = SolicitacaoAmizade.objects.filter(para_usuario=request.user, aceita=False)
    return render(request, 'listar_solicitacoes.html', {'solicitacoes_recebidas': solicitacoes_recebidas})

def aceitar_solicitacao(request, solicitacao_id):
    solicitacao = SolicitacaoAmizade.objects.get(pk=solicitacao_id)
    solicitacao.aceita = True
    solicitacao.save()
    return redirect('listar_amigos')

def recusar_solicitacao(request, solicitacao_id):
    solicitacao = SolicitacaoAmizade.objects.get(pk=solicitacao_id)
    solicitacao.delete()
    return redirect('listar_amigos')
