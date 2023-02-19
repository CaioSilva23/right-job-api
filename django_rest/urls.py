from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ROTAS PARA A API
    path('api/', include('api.urls')),

    # ROTAS PARA AUTENTICACAO
]
