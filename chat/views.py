from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from home.models import Campanha, Perfil
from .models import Grupo, Mensagem, SolicitacaoEntrada


@login_required
def Novo_grupo(request):
    u = request.user
    new = Grupo.objects.create(criador=u, publico=True)
    new.membros.add(u)
    new.save()
    print("Novo grupo criado com sucesso:", new.uuid) 
    return redirect('criarCampanhas')


@login_required
def Entrar_grupo(request, uuid):
	u = request.user
	gp = Grupo.objects.get(uuid=uuid)
	gp.membros.add(u)
	gp.save()
	return redirect('buscarmesa')


@login_required
def Sair_grupo(request, uuid):
	u = request.user
	gp = Grupo.objects.get(uuid=uuid)
	gp.membros.remove(u)
	gp.save()
	return redirect('buscarmesa')


@login_required
def Abrir_chat_pub(request, uuid):
	grupo = Grupo.objects.get(uuid=uuid)
	if request.user not in grupo.membros.all():
		return HttpResponseForbidden('não é um membro')
	mensagens = Mensagem.objects.filter(grupo=grupo).order_by('tempo')
	return render(request, 'chat.html', context={'mensagens':mensagens, 'uuid': uuid})


@login_required
def Remover_grupo(request, uuid):
    u = request.user
    grupo = Grupo.objects.get(uuid=uuid)
    

    if grupo.criador != u:
        return HttpResponseForbidden('Você não tem permissão para excluir este grupo.')
    
    grupo.delete()
    return redirect('buscarmesa')

@login_required
def excluir_mensagem_pub(request, mensagem_id):
    mensagem = get_object_or_404(Mensagem, pk=mensagem_id)

    if mensagem.autor == request.user:
        grupo = mensagem.grupo
        if grupo:
            grupo_uuid = grupo.uuid  
            mensagem.delete()  
            return redirect('Abrir_chat_pub', uuid=grupo_uuid) 

    return HttpResponseForbidden("Você não tem permissão para excluir esta mensagem.")

def gerenciar_solicitacoes(request, campanha_id=None):
    if campanha_id:
        # Recupera a campanha com base no campanha_id
        campanha = Campanha.objects.get(pk=campanha_id)

        # Verifica se o usuário autenticado é o mestre da campanha
        if campanha.nomeMestre.nomePerfil != request.user:
            return redirect('buscarmesa')

        # Recupera as solicitações de entrada relacionadas à campanha
        solicitacoes = SolicitacaoEntrada.objects.filter(para_campanha=campanha)
    else:
        # Caso não haja um campanha_id, listamos todas as solicitações de entrada
        solicitacoes = SolicitacaoEntrada.objects.all()

    context = {
        'campanha': campanha if campanha_id else None,
        'solicitacoes': solicitacoes,
    }

    return render(request, 'principal/gerenciar_solicitacoes.html', context)


def enviar_solicitacao(request, campanha_id):
    campanha = Campanha.objects.get(pk=campanha_id)
    de_usuario = Perfil.objects.get(nomePerfil=request.user)
    
    
    if de_usuario:
        solicitacao = SolicitacaoEntrada.objects.create(
            de_usuario=de_usuario,
            para_campanha=campanha,
            status='Pendente'
        )
        return redirect('buscarmesa')
    else:
         return HttpResponseForbidden("Perfil não existe ou foi apagado")

    
from django.http import Http404

def aceitar_solicitacao_camp(request, solicitacao_id):
    try:
        solicitacao = SolicitacaoEntrada.objects.get(pk=solicitacao_id)
        solicitacao.status = 'Aceita'
        solicitacao.save()
        return redirect('buscarmesa')
    except SolicitacaoEntrada.DoesNotExist:
        raise Http404("Solicitação não encontrada")

def recusar_solicitacao_camp(request, solicitacao_id):
    try:
        solicitacao = SolicitacaoEntrada.objects.get(pk=solicitacao_id)
        solicitacao.status = 'Recusada'
        solicitacao.save()
        return redirect('buscarmesa')
    except SolicitacaoEntrada.DoesNotExist:
        raise Http404("Solicitação não encontrada")
