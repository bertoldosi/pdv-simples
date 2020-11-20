from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome do produto', max_length=100)
    quantidade = models.IntegerField('Quantidade')

    def __str__(self):
        return self.nome