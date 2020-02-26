from django.contrib import admin
from django.contrib.admin import site
from django.contrib.admin import ModelAdmin
from .models import Tarefa


class TarefaAdmin(ModelAdmin):
    fields = ['nome','descricao', 'status']
    list_display = ['nome', 'descricao', 'data_de_criacao','data_de_execucao', 'status']
    list_editable = ['status']


admin.site.register(Tarefa, TarefaAdmin)
