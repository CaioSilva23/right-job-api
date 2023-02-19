from django.urls import path
from .views import tecnolgia_views
from .views import vaga_views

urlpatterns = [

    # ROTAS PARA TECNOLOGIAS
    path('tecnologias/', tecnolgia_views.TecnologiasList.as_view(), name='tecnologia-list'),
    path('tecnologias/<int:id>', tecnolgia_views.TecnologiaDetail.as_view(), name='tecnologia-datail'),

    # ROTAS PARA VAGAS
    path('vagas/', vaga_views.VagaList.as_view(), name='vaga-list'),
    path('vagas/<int:id>', vaga_views.VagaDetail.as_view(), name='vaga-detail'),
]
