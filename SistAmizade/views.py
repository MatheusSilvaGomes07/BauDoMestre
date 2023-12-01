from django.http import HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

from home.models import Perfil
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

    solicitacao = SolicitacaoAmizade.objects.filter(de_usuario=request.user, para_usuario=amigo).first()
    if solicitacao:
        solicitacao.delete()

    return redirect('listar_amigos')


def listar_amigos(request):
    amigos = Amigo.objects.filter(usuario=request.user)

    return render(request, 'listar_amigos.html', {'amigos': amigos})


def enviar_solicitacao(request, user_id):
    para_usuario = User.objects.get(pk=user_id)
    usuario = Perfil.objects.get(pk=user_id)
    # Verificar se já existe uma solicitação pendente
    solicitacao_pendente = SolicitacaoAmizade.objects.filter(de_usuario=request.user, para_usuario=para_usuario, aceita=False).first()

    if solicitacao_pendente:
        # Se há uma solicitação pendente, você pode fornecer uma mensagem ou redirecionar para uma página informando ao usuário
        # Exemplo de mensagem flash (requer 'messages' no seu settings.py)
        return HttpResponseNotFound(request, f"Você já enviou uma solicitação de amizade para {para_usuario.username}. Aguarde a resposta do usuário.")
        

    # Se não houver uma solicitação pendente, crie uma nova
    solicitacao, criada = SolicitacaoAmizade.objects.get_or_create(de_usuario=request.user, para_usuario=para_usuario)

    # Verificar se a solicitação foi criada ou já existia
    if criada:
        return redirect('exibir_perfil', usuario.slug)
    else:
        # Tratar o caso em que a solicitação já existe (opcional)
        # Por exemplo, exibir uma mensagem de erro
        return redirect('listar_amigos')

def listar_solicitacoes(request):
    solicitacoes_recebidas = SolicitacaoAmizade.objects.filter(para_usuario=request.user, aceita=False)
    return render(request, 'listar_solicitacoes.html', {'solicitacoes_recebidas': solicitacoes_recebidas})

def aceitar_solicitacao(request, solicitacao_id):
    solicitacao = SolicitacaoAmizade.objects.get(pk=solicitacao_id)
    solicitacao.aceita = True
    solicitacao.delete()

    grupo_id = f"{solicitacao.de_usuario.id}_{solicitacao.para_usuario.id}"

    grupo_chat, _ = Grupo.objects.get_or_create(criador=solicitacao.de_usuario, uuid_pers=grupo_id, publico=False)
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
    amigos = Amigo.objects.filter(usuario=user)

    aux = Perfil.objects.get(id=user_id)

    
    chatPerfil = {
        'fotoConta': aux.fotoConta,
        'nome': amigo.username,
        'tipoJogador': aux.tipo_player,
        'slug': aux.slug
    }


    grupo = Grupo.objects.filter(membros=user).filter(membros=amigo).first()

    if not grupo:
        grupo, _ = Grupo.objects.get_or_create(criador=user, publico=False)
        grupo.membros.add(user, amigo)
        grupo.save()

    if not Amigo.objects.filter(usuario=user, amigo=amigo).exists():
        return HttpResponseForbidden('Você não é amigo desse usuário.')

    mensagens = Mensagem.objects.filter(grupo=grupo).order_by('tempo')

    for teste in amigos:
        
        combinacao1 = f'{teste.amigo.id}_{user.id}'
        combinacao2 = f'{user.id}_{teste.amigo.id}'

        try:
            gp = Grupo.objects.get(uuid_pers = combinacao1)
        except:
            gp = Grupo.objects.get(uuid_pers = combinacao2)


        ultimaMSG = Mensagem.objects.filter(grupo=gp).order_by('-id').first()
        
        if ultimaMSG:
            teste.lastMessage = f'{ultimaMSG.autor}: {ultimaMSG.conteudo}'
            teste.lastHour = ultimaMSG.tempo

    return render(request, 'chat-privado.html', context={'mensagens': mensagens, 'uuid': grupo.uuid, 'amigos': amigos, 'chatPerfil': chatPerfil})

def excluir_mensagem_priv(request, mensagem_id):
    mensagem = get_object_or_404(Mensagem, pk=mensagem_id)

    if mensagem.autor == request.user:
        mensagem.delete()

    return redirect('Abrir_chat_privado', user_id=mensagem.grupo.membros.exclude(id=request.user.id).first().id)


def listar_amigos_usuario(request, user_id):
    usuario = User.objects.get(pk=user_id)
    amigos = Amigo.objects.filter(usuario=usuario)

    return render(request, 'listar_amigos_usuario.html', {'usuario': usuario, 'amigos': amigos})

    


    
