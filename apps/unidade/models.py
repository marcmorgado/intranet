from django.db import models

class Unidade(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da Unidade')

    def __str__(self):
        return self.nome