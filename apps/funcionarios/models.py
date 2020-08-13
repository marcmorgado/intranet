from django.db import models
from django.contrib.auth.models import User
from apps.setores.models import Setor
from apps.unidade.models import Unidade

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    setores = models.ManyToManyField(Setor)
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT)


def __str__(self):
        return self.nome