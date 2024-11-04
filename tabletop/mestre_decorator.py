from functools import wraps
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from home.models import Campanha

def is_mestre(func):
   @wraps(func)
   def wrapper(request, *args, **kwargs):
      campaign_id = kwargs.get('campaign_id')
      campanha = get_object_or_404(Campanha, id=campaign_id)

      if campanha.nomeMestre.id == request.user.id:
        kwargs['is_mestre'] = True
      else:
         kwargs['is_mestre'] = False
      return func(request, *args, **kwargs)
         
   return wrapper
