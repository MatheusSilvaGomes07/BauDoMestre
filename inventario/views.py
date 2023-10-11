from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
import os
from inventario.forms import PastaForm, FileForm
from inventario.models import Pasta, File
from django.contrib import messages
import magic

@login_required
def index(request):
    return render(request, 'inventario/index.html')


@login_required
def mapas(request):
    div = 'Mapas'
    user = request.user
    pastas = Pasta.objects.filter(owner=user, divisao=div)
    mensagem = ''
    
    
    if request.method == 'POST':
        form = PastaForm(request.POST)
        if form.is_valid():
            validation = form.save(commit=False)
            if Pasta.objects.filter(owner=user, divisao=div, nome=validation.nome).exists():
                mensagem = "Não é possível criar pastas com o mesmo nome"
            else:
                validation.owner = user
                validation.divisao = div
                validation.save()
                return redirect('mapas')
    else:
        form = PastaForm()

    return render(request, 'inventario/divisao.html', {'form': form, 'pastas': pastas, 'div': div, 'mensagem': mensagem})

@login_required
def criaturas(request):
    div = 'Criaturas'
    user = request.user
    pastas = Pasta.objects.filter(owner=user, divisao=div)
    mensagem = ''

    if request.method == 'POST':
        form = PastaForm(request.POST)
        if form.is_valid():
            validation = form.save(commit=False)
            if Pasta.objects.filter(owner=user, divisao=div, nome=validation.nome).exists():
                mensagem = "Não é possível criar pastas com o mesmo nome"
            else:
                validation.owner = user
                validation.divisao = div
                validation.save()
                return redirect('criaturas')
    else:
        form = PastaForm()

    return render(request, 'inventario/divisao.html', {'form': form, 'pastas': pastas, 'div': div, 'mensagem':mensagem})

@login_required
def documentos(request):
    div = 'Documentos'
    user = request.user
    pastas = Pasta.objects.filter(owner=user, divisao=div)
    mensagem = ''

    if request.method == 'POST':
        form = PastaForm(request.POST)
        if form.is_valid():
            validation = form.save(commit=False)
            if Pasta.objects.filter(owner=user, divisao=div, nome=validation.nome).exists():
                mensagem = "Não é possível criar pastas com o mesmo nome"
            else:
                validation.owner = user
                validation.divisao = div
                validation.save()
                return redirect('documentos')
    else:
        form = PastaForm()

    return render(request, 'inventario/divisao.html', {'form': form, 'pastas': pastas, 'div': div, 'mensagem': mensagem})

@login_required
def imagens(request):
    div = 'Imagens'
    user = request.user
    pastas = Pasta.objects.filter(owner=user, divisao=div)
    mensagem = ''
    
    if request.method == 'POST':
        form = PastaForm(request.POST)
        if form.is_valid():
            validation = form.save(commit=False)
            if Pasta.objects.filter(owner=user, divisao=div, nome=validation.nome).exists():
                mensagem = "Não é possível criar pastas com o mesmo nome"
            else:
                validation.owner = user
                validation.divisao = div
                validation.save()
                return redirect('imagens')
    else:
        form = PastaForm()

    return render(request, 'inventario/divisao.html', {'form': form, 'pastas': pastas, 'div': div, 'mensagem': mensagem})

@login_required
def musicas(request):
    div = 'Musicas'
    user = request.user
    pastas = Pasta.objects.filter(owner=user, divisao=div)
    mensagem = ''
    if request.method == 'POST':
        form = PastaForm(request.POST)
        if form.is_valid():
            validation = form.save(commit=False)
            if Pasta.objects.filter(owner=user, divisao=div, nome=validation.nome).exists():
                mensagem = "Não é possível criar pastas com o mesmo nome"
            else:
                validation.owner = user
                validation.divisao = div
                validation.save()
                return redirect('musicas')
    else:
        form = PastaForm()

    return render(request, 'inventario/divisao.html', {'form': form, 'pastas': pastas, 'div': div, 'mensagem': mensagem})



@login_required
def visualizar_pasta(request, div, pasta):
    
    user = request.user
    pastas = Pasta.objects.get(nome=pasta, owner=user, divisao=div)
    files = File.objects.filter(owner=user, pasta=pastas.id)
    base_name = ''
    mime = magic.Magic()
    mensagem = True
    

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            files = form.cleaned_data["file"]

            for f in files:
                base_name, extension = os.path.splitext(str(f))
                file_type = mime.from_buffer(f.read(1024))

                if 'image' in file_type or 'PDF document' in file_type or 'GIF image' in file_type:
                    arquivo = File(file=f, owner=user, pasta=pastas, nome=base_name)
                    arquivo.save()
                else:
                    mensagem = False
    

                
            return redirect('visualizar_pasta', div, pasta)
    else:
        form = FileForm()
    print(mensagem)
    return render(request, 'inventario/visualizar_pasta.html', {'files': files, 'form': form})

@login_required
def deletar_pasta(request, id):
    
     
    delete = get_object_or_404(Pasta, id=id)
    divisao = delete.divisao
    
    delete.delete()
    return redirect(divisao.lower())
