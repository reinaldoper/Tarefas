from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, ForeignKey
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import TextField
from django.test import Client


# Create your models here.


class Tarefa(Model):
    data_de_criacao = DateTimeField(auto_now_add=True, verbose_name='data de criação')
    data_de_execucao = DateTimeField(auto_now=True, verbose_name='data de execução')
    nome = CharField(max_length=200, verbose_name='nome')
    descricao = TextField(verbose_name='descrição', null=True, blank=True)
    status = BooleanField(default=False, verbose_name='finalizado')

    class Meta:
        ordering = ['data_de_criacao']

    def __str__(self):
        return self.description
