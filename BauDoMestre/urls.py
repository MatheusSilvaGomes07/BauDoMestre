from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from home.views import CustomSignupView, CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/signup/', CustomSignupView.as_view(), name='custom_signup'),
    path('accounts/login/', CustomLoginView.as_view(), name='custom_login'),
    path('meus-personagens/', include('meus_personagens.urls')),
    path('chat/', include('chat.urls')),
    path('inventario/', include('inventario.urls')),
    path('SistAmizade/', include('SistAmizade.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'home.views.handler404'
