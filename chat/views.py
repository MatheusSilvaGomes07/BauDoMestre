from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponseForbidden, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
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
	return render(request, 'chat.html', context={'mensagens':mensagens, 'uuid': uuid, 'grupo': grupo})


@login_required
def Remover_grupo(request, uuid):
    u = request.user
    grupo = Grupo.objects.get(uuid=uuid)
    

    if grupo.criador != u:
        return HttpResponseForbidden('Você não tem permissão para excluir este grupo.')
    
    campanha = grupo.campanha
    
    grupo.delete()
    
    if campanha:
        campanha.delete()
        
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

@login_required
def gerenciar_solicitacoes(request, campanha_id=None):
    from home.models import Campanha

    campanha = None  # Defina campanha como None inicialmente

    campanhas_do_mestre = Campanha.objects.filter(nomeMestre__nomePerfil=request.user)

    if campanha_id:
        # Se campanha_id for fornecido, filtre apenas para a campanha específica
        campanha = get_object_or_404(Campanha, pk=campanha_id)
        solicitacoes = SolicitacaoEntrada.objects.filter(para_campanha=campanha, aceita=False, status='Pendente')
    else:
        # Se não houver campanha_id, filtre as solicitações para todas as campanhas do mestre
        if campanha and campanha.nomeMestre.nomePerfil != request.user:
            return redirect('buscarmesa')

        solicitacoes = SolicitacaoEntrada.objects.filter(para_campanha__in=campanhas_do_mestre, aceita=False, status='Pendente')

    context = {
        'campanha': campanha,
        'solicitacoes': solicitacoes,
    }

    return render(request, 'principal/gerenciar_solicitacoes.html', context)


def enviar_solicitacao(request, campanha_id):
    from home.models import Campanha, Perfil
    campanha = Campanha.objects.get(pk=campanha_id)
    de_usuario = Perfil.objects.get(nomePerfil=request.user)

    # Verifica se já existe uma solicitação pendente
    solicitacao_pendente = SolicitacaoEntrada.objects.filter(de_usuario=de_usuario, para_campanha=campanha, status='Pendente').first()

    if solicitacao_pendente:
        return HttpResponseForbidden("Você já possui uma solicitação pendente para esta campanha.")

    solicitacao = SolicitacaoEntrada.objects.create(
        de_usuario=de_usuario,
        para_campanha=campanha,
        status='Pendente'
    )
    
    return redirect('buscarmesa')


def aceitar_solicitacao_camp(request, solicitacao_id):
    try:
        solicitacao = SolicitacaoEntrada.objects.get(pk=solicitacao_id)
        solicitacao.aceitar_solicitacao()

        # Adicione um print para verificar a campanha associada à solicitação
        print(f"Campanha associada à solicitação: {solicitacao.para_campanha.nomeCampanha}")

        return redirect('buscarmesa')

    except SolicitacaoEntrada.DoesNotExist:
        return HttpResponseNotFound("Solicitação não encontrada")

    
def recusar_solicitacao_camp(request, solicitacao_id):
    try:
        solicitacao = SolicitacaoEntrada.objects.get(pk=solicitacao_id)
        solicitacao.status = 'Recusada'
        solicitacao.delete()
        return redirect('buscarmesa')
    except SolicitacaoEntrada.DoesNotExist:
        raise Http404("Solicitação não encontrada")
    
    