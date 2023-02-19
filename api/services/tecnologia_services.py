from ..models import Tecnologia
from django.shortcuts import get_object_or_404


def listar_tecnologias():
    tecnologias = Tecnologia.objects.all()
    return tecnologias

def listar_tecnologia_id(id: int) -> object:
    tecnologia = get_object_or_404(Tecnologia, id=id)
    return tecnologia
 
def cadastrar_tecnologia(nova_tecnologia: object) -> object:
    tecnologia = Tecnologia(nome=nova_tecnologia.nome).save()
    return tecnologia

def editar_tecnologia(antiga_tecnologia, nova_tecnologia) -> object:
    antiga_tecnologia.nome = nova_tecnologia.nome
    antiga_tecnologia.save(force_update=True)

def remover_tecnologia(id):
    tecnologia_remover = listar_tecnologia_id(id)
    tecnologia_remover.delete()
