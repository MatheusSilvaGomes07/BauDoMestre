from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from chat.models import Grupo

def user_in_group(view_func):
    @login_required
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        campaign_id = kwargs.get('campaign_id')  # Obtém o ID da campanha da URL

        # Verifica se existe um grupo associado à campanha e se o usuário é membro
        if Grupo.objects.filter(campanha_id=campaign_id, membros=user).exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('buscarmesa')  # Redireciona para uma página de acesso negado

    return _wrapped_view
