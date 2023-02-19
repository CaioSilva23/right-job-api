from django.urls import path
from .views import tecnolgia_views, vaga_views, usuario_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [

    # ROTAS PARA TECNOLOGIAS
    path('tecnologias/', tecnolgia_views.TecnologiasList.as_view(), name='tecnologia-list'),
    path('tecnologias/<int:id>', tecnolgia_views.TecnologiaDetail.as_view(), name='tecnologia-datail'),

    # ROTAS PARA VAGAS
    path('vagas/', vaga_views.VagaList.as_view(), name='vaga-list'),
    path('vagas/<int:id>', vaga_views.VagaDetail.as_view(), name='vaga-detail'),

    #USUÁRIOS
    path('usuarios/', usuario_views.UsuarioList.as_view(), name='usuario-list'),

    # AUTENTICAÇÃO
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
