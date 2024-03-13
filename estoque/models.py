from django.db import models
from django.utils.text import slugify
# from secrets import token_urlsafe

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.FloatField()
    quantidade = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    # token = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nome
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)

        '''Pode ser utilizado o slug ou o token para visualizar na URL'''
        # if not self.token:
        #     self.token = token_urlsafe(16)

        super().save(*args, **kwargs)

