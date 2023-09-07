from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Grupo


# Create your views here.
@login_required
def Novo_grupo(request):
	u = request.user
	new = Grupo.objects.create()
	new.membros.add(u)
	new.save()
	return redirect('principal/home.html')


@login_required
def Entrar_grupo(request, uuid):
	u = request.user
	gp = Grupo.objects.get(uuid=uuid)
	gp.membros.add(u)
	gp.save()
	return redirect('principal/home.html')


@login_required
def Sair_grupo(request, uuid):
	u = request.user
	gp = Grupo.objects.get(uuid=uuid)
	gp.membros.remove(u)
	gp.save()
	return redirect('principal/home.html')


@login_required
def Abrir_chat(request, uuid):
	grupo = Grupo.objects.get(uuid=uuid)
	if request.user not in grupo.membros.all():
		return HttpResponseForbidden('Not a member. Try another group.')
	mensagens = grupo.mensagens_set.all()
	sorted_messages = sorted(mensagens, key=lambda x: x.tempo)
	return render(request, 'chat.html', context={'messages':sorted_messages, 'uuid': uuid})


@login_required
def Remover_grupo(request, uuid):
	u = request.user
	Grupo.objects.get(uuid=uuid).delete()
	return redirect('principal/home.html')
