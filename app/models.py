"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=200)
    periodo = models.CharField(max_length=50)
    instituicao = models.CharField(max_length=200)

class Vestibular(models.Model):
    nome = models.CharField(max_length=200)

class Candidato(models.Model):
    nome = models.CharField(max_length=200)
    rg = models.CharField(max_lenght=9)
    cpf = models.CharField(max_lenght=11)
    endereço = models.CharField(max_lenght=100)
    telefone = models.CharField(max_lenght=12)

class LocalProva(models.Model):
    nome_escola = models.CharField(max_length=200)
    endereço = models.CharField(max_lenght=100)
    cidade = models.CharField(max_lenght=70)
    estado = models.CharField(max_lenght=2)
    

