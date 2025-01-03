from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
import os
from home.models import Perfil
from inventario.forms import PastaForm, FileForm
from inventario.models import Pasta, File
from django.contrib import messages
import magic

@login_required
def index(request):
    user = request.user
    perfil = Perfil.objects.get(nomePerfil=request.user)


    mapas_count = Pasta.objects.filter(owner=user, divisao='Mapas').count()
    criaturas_count = Pasta.objects.filter(owner=user, divisao='Criaturas').count()
    documentos_count = Pasta.objects.filter(owner=user, divisao='Documentos').count()
    imagens_count = Pasta.objects.filter(owner=user, divisao='Imagens').count()
    musicas_count = Pasta.objects.filter(owner=user, divisao='Musicas').count()


    return render(request, 'inventario/index.html', {
        'fotoConta': perfil.fotoConta,
        'mapas_count': mapas_count,
        'criaturas_count': criaturas_count,
        'documentos_count': documentos_count,
        'imagens_count': imagens_count,
        'musicas_count': musicas_count
        })


@login_required
def mapas(request):

    perfil = Perfil.objects.get(nomePerfil=request.user)
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

    return render(request, 'inventario/divisao.html', {'form': form, 'pastas': pastas, 'div': div, 'mensagem': mensagem, 'fotoConta': perfil.fotoConta})

@login_required
def criaturas(request):
    perfil = Perfil.objects.get(nomePerfil=request.user)
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

    return render(request, 'inventario/divisao.html', {'form': form, 'pastas': pastas, 'div': div, 'mensagem':mensagem, 'fotoConta': perfil.fotoConta})

@login_required
def documentos(request):
    perfil = Perfil.objects.get(nomePerfil=request.user)
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

    return render(request, 'inventario/divisao.html', {'form': form, 'pastas': pastas, 'div': div, 'mensagem': mensagem, 'fotoConta': perfil.fotoConta})

@login_required
def imagens(request):
    perfil = Perfil.objects.get(nomePerfil=request.user)
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

    return render(request, 'inventario/divisao.html', {'form': form, 'pastas': pastas, 'div': div, 'mensagem': mensagem, 'fotoConta': perfil.fotoConta})

@login_required
def musicas(request):
    perfil = Perfil.objects.get(nomePerfil=request.user)
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

    return render(request, 'inventario/divisao.html', {'form': form, 'pastas': pastas, 'div': div, 'mensagem': mensagem, 'fotoConta': perfil.fotoConta})

def verificar_extensao(div, file_type, request, tamanho, extension):
    # Convertendo a extensão para minúsculas para garantir a comparação consistente
    extension = extension.lower()

    if div == "Mapas":
        if 'image' in file_type or 'PDF document' in file_type or 'GIF image' in file_type:
            return True
        else:
            messages.info(request, "A divisão de mapas só aceita documentos de imagem, GIFs e PDFs")
            return False

    if div == "Criaturas":
        if 'image' in file_type or 'PDF document' in file_type or 'GIF image' in file_type or 'Microsoft Word' in file_type or 'RAR archive' in file_type or 'Zip archive' in file_type :
            return True
        else:
            messages.info(request, "Foi identificado um possível arquivo malicioso ou que não seja possível seu envio, tente enviar novamente")
            return False

    if div == "Documentos":
        if 'image' in file_type or 'PDF document' in file_type or 'GIF image' in file_type or 'Microsoft Word' in file_type or 'RAR archive' in file_type or 'Zip archive' in file_type:
            return True
        else:
            messages.info(request, "Foi identificado um possível arquivo malicioso ou que não seja possível seu envio, tente enviar novamente")
            return False

    if div == "Imagens":
        if 'image' in file_type or 'GIF image' in file_type:
            return True
        else:
            messages.info(request, "A divisão de imagens só aceita arquivos de imagens e GIFs")
            return False

    if div == "Musicas":
        # Verifica a extensão diretamente, sem depender do tipo MIME
        if extension in ['.mp3', '.wav', '.ogg']:
            return True
        else:
            messages.info(request, "A divisão de músicas só aceita arquivos de áudios")
            return False

    if tamanho > 83886080:  # 80MB
        messages.info(request, "Algum arquivo enviado era maior que 80MB, só é possível o envio de arquivos abaixo de 80MB")
        return False

    # Caso não se enquadre em nenhuma das divisões
    messages.info(request, "Tipo de arquivo não permitido.")
    return False



@login_required
def visualizar_pasta(request, div, pasta):
    perfil = Perfil.objects.get(nomePerfil=request.user)
    user = request.user
    pastas = Pasta.objects.get(nome=pasta, owner=user, divisao=div)

    pastas_sessao = Pasta.objects.filter(owner=user, divisao=div)

    for p in pastas_sessao:
        print(p.nome)

    files = File.objects.filter(owner=user, pasta=pastas.id)
    base_name = ''
    mime = magic.Magic()

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            files = form.cleaned_data["file"]

            for f in files:
                base_name, extension = os.path.splitext(str(f))
                file_type = mime.from_buffer(f.read(1024))
                tamanho = f.size



                if verificar_extensao(div, file_type, request, tamanho, extension):
                    arquivo = File(file=f, owner=user, pasta=pastas, nome=base_name, tamanho=tamanho, extensao=extension)
                    arquivo.save()


            return redirect('visualizar_pasta', div, pasta)
    else:
        form = FileForm()
    return render(request, 'inventario/visualizar_pasta.html', {'files': files, 'form': form, 'div': div, 'pasta':pasta, 'fotoConta': perfil.fotoConta, 'pastas_sessao': pastas_sessao,})

@login_required
def deletar_arquivo(request, id, div, id_pasta):
    pasta = Pasta.objects.get(id=id_pasta)
    user = request.user

    if user == pasta.owner or user.is_staff:
        delete = get_object_or_404(File, id=id)
        delete.delete()

    return redirect('visualizar_pasta', div, pasta.nome)

@login_required
def edit_pasta(request, id_pasta):
    pasta = get_object_or_404(Pasta, pk=id_pasta)
    user = request.user

    if user == pasta.owner or user.is_staff():
        if request.method == 'POST':
            form = PastaForm(request.POST, instance=pasta)
            if form.is_valid():
                form.save()
                return redirect('divisoes')
        else:
            form = PastaForm(instance=pasta)
    else:
        return redirect('divisoes')

    return render(request, 'inventario/divisao.html', {'form': form})




@login_required
def deletar_pasta(request, id):
    pasta_owner = Pasta.objects.get(id=id).owner
    user = request.user


    if user == pasta_owner or user.is_staff:
        delete = get_object_or_404(Pasta, id=id)
        divisao = delete.divisao
        delete.delete()

        return redirect(divisao.lower())
    else:
        return redirect('divisoes')

