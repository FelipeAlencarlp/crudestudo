from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.FloatField()
    quantidade = models.IntegerField()

    def __str__(self) -> str:
        return self.nome
