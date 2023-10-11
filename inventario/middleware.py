from django.http import HttpResponseForbidden
from django.contrib import messages

class MaliciousFileCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST' and request.FILES:
            for file in request.FILES.values():
                # Verifique a extensão do arquivo
                if file.name.endswith(('.exe', '.bat', '.vbs', '.js', '.jar', '.php', '.html', '.dll', '.sh', '.py', '.asp', '.aspx', '.sql')):
                    messages.error(request, "A extensão do arquivo é perigosa. Faça o upload de um arquivo seguro.")
                        

        return self.get_response(request)