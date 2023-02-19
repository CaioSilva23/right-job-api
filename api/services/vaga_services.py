from ..models import Vaga
from django.shortcuts import get_object_or_404
from .tecnologia_services import listar_tecnologia_id

def listar_vagas():
    vagas = Vaga.objects.all()
    return vagas 

def listar_vaga_id(id):
    vaga = get_object_or_404(Vaga, id=id)
    return vaga

def cadastrar_vaga(nova_vaga):
    vaga = Vaga(titulo=nova_vaga.titulo,
                descricao=nova_vaga.descricao, 
                salario=nova_vaga.salario, 
                tipo_contratacao=nova_vaga.tipo_contratacao, 
                local=nova_vaga.local, 
                quantidade=nova_vaga.quantidade, 
                contato=nova_vaga.contato, 
                )
    vaga.save()
    techs = [listar_tecnologia_id(i.id) for i in nova_vaga.tecnologias]
    vaga.tecnologias.add(*techs)
    return vaga

def editar_vaga(vaga_antiga, vaga_nova):
    vaga_antiga.titulo = vaga_nova.titulo
    vaga_antiga.descricao = vaga_nova.descricao
    vaga_antiga.salario = vaga_nova.salario
    vaga_antiga.tipo_contratacao = vaga_nova.tipo_contratacao
    vaga_antiga.local = vaga_nova.local
    vaga_antiga.quantidade = vaga_nova.quantidade
    vaga_antiga.contato = vaga_nova.contato
    vaga_antiga.tecnologias.set(vaga_nova.tecnologias)
    vaga_antiga.save(force_update=True)
    return vaga_antiga
    

def remover_vaga(id):
    vaga = listar_vaga_id(id)
    vaga.delete()