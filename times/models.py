from django.db import models

# Create your models here.

class Jogadores(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    idade = models.IntegerField(blank=False, null=False)
    posicao = models.CharField(max_length=50, blank=False, null=False)
    numero = models.IntegerField(blank=False, null=False)
    time = models.CharField(max_length=50, blank=False, null=False)
    nacionalidade = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome
