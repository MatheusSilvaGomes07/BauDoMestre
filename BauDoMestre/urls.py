from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('allauth.urls')),
    path('meus-personagens/', include('meus_personagens.urls')),
    path('chat/', include('chat.urls'))
]

handler404 = 'home.views.handler404'