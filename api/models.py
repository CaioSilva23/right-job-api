from django.db import models


class Tecnologia(models.Model):
    nome = models.CharField(max_length=20, null=False, blank=False)

class Vaga(models.Model):

    contatacao_choices = (
    ('PJ', 'PJ'),
    ('CLT', 'CLT'),
    )

    titulo = models.CharField(max_length=50, null=True, blank=True)
    descricao = models.TextField(null=False, blank=False)
    salario = models.FloatField(null=True, blank=False)
    local = models.CharField(max_length=20, null=False, blank=False)
    quantidade = models.IntegerField(null=False, blank=False)
    contato = models.EmailField(null=False, blank=False)
    tipo_contratacao = models.CharField(max_length=3, null=False, blank=False, choices=contatacao_choices)
    tecnologias = models.ManyToManyField(Tecnologia)

    def __str__(self) -> str:
        return self.titulo