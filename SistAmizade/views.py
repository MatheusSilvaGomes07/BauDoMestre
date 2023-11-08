from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .models import SolicitacaoAmizade, Amigo
from django.contrib.auth.models import User
from chat.models import Grupo, Mensagem
from django.contrib.auth.decorators import login_required

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
    solicitacao = SolicitacaoAmizade(de_usuario=request.user, para_usuario=para_usuario)
    solicitacao.save()
    return redirect('listar_amigos')

def listar_solicitacoes(request):
    solicitacoes_recebidas = SolicitacaoAmizade.objects.filter(para_usuario=request.user, aceita=False)
    return render(request, 'listar_solicitacoes.html', {'solicitacoes_recebidas': solicitacoes_recebidas})

def aceitar_solicitacao(request, solicitacao_id):
    solicitacao = SolicitacaoAmizade.objects.get(pk=solicitacao_id)
    solicitacao.aceita = True
    solicitacao.save()

    grupo_chat, _ = Grupo.objects.get_or_create(criador=solicitacao.de_usuario, publico=False)
    grupo_chat.membros.add(solicitacao.de_usuario, solicitacao.para_usuario)
    grupo_chat.save()
    
    if not Amigo.objects.filter(usuario=solicitacao.de_usuario, amigo=solicitacao.para_usuario).exists():
        Amigo.objects.create(usuario=solicitacao.de_usuario, amigo=solicitacao.para_usuario)
    
    if not Amigo.objects.filter(usuario=solicitacao.para_usuario, amigo=solicitacao.de_usuario).exists():
        Amigo.objects.create(usuario=solicitacao.para_usuario, amigo=solicitacao.de_usuario)

    return redirect('listar_amigos')

def recusar_solicitacao(request, solicitacao_id):
    solicitacao = SolicitacaoAmizade.objects.get(pk=solicitacao_id)
    solicitacao.delete()
    return redirect('listar_amigos')

@login_required
def Abrir_chat_Amigo(request, user_id):
    user = request.user
    amigo = User.objects.get(pk=user_id)

    grupo = Grupo.objects.filter(membros=user).filter(membros=amigo).first()

    if not grupo:
        grupo, _ = Grupo.objects.get_or_create(criador=user, publico=False)
        grupo.membros.add(user, amigo)
        grupo.save()

    if not Amigo.objects.filter(usuario=user, amigo=amigo).exists():
        return HttpResponseForbidden('Você não é amigo desse usuário.')

    mensagens = Mensagem.objects.filter(grupo=grupo).order_by('tempo')
    return render(request, 'chat-privado.html', context={'mensagens': mensagens, 'uuid': grupo.uuid})

def excluir_mensagem_priv(request, mensagem_id):
    mensagem = get_object_or_404(Mensagem, pk=mensagem_id)

    if mensagem.autor == request.user:
        mensagem.delete()

    return redirect('Abrir_chat_privado', user_id=mensagem.grupo.membros.exclude(id=request.user.id).first().id)


    
  

    


    
