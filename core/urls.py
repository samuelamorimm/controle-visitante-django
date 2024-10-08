
from django.contrib import admin
from django.urls import path
from dashboard.views import index
from visitantes.views import registrar_visitante, informacoes_visitante, finalizar_visita
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index ,name='index'),
    path('registrar-visitante/', registrar_visitante ,name='registrar_visitante'),
    path('informacoes-visitante/<int:pk>', informacoes_visitante, name='informacoes_visitante'),
    path('visitante/<int:pk>/finalizar-visita', finalizar_visita, name='finalizar_visita'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name='login'),
]
