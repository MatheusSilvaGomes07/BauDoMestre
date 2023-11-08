from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Grupo, Mensagem


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



