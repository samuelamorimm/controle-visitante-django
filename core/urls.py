
from django.contrib import admin
from django.urls import path
from dashboard.views import index
from visitantes.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index ,name='index'),
    path('registrar-visitante/', register, name='registrar_visitante')
]
