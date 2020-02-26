import self
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.dates import ArchiveIndexView

from .forms import FormTarefa
from .models import Tarefa
from django.views.generic import View, DetailView, DeleteView, UpdateView
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template.context import RequestContext
from . import forms
from django.views.decorators.csrf import csrf_exempt


class TarefasView(ArchiveIndexView):
    model = Tarefa
    template_name = 'tarefas/tarefa_archive.html'
    date_field = 'data_de_criacao'


class TarefaDetail(DetailView):
    model = Tarefa
    template_name = 'tarefas/detalhes.html'


class Home(View):
    template_name = 'tarefas/home.html'
    context = {}
    context['counter'] = Tarefa.objects.filter(status=True).count()

    def get(self, request, *args, **kwargs):
        return render_to_response(self.template_name, self.context, RequestContext(request))


class AdicionaTarefa(View):
    template_name = 'tarefas/cria_tarefa.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = FormTarefa()
        return render_to_response(self.template_name, self.context,
                                  RequestContext(request))

    def post(self, request, *args, **kwargs):
        form = FormTarefa(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tarefas/')
        else:
            self.context['form'] = form
            return render_to_response(self.template_name, self.context, RequestContext(request))


class DeleteTarefa(DeleteView):
    template_name = 'tarefas/deletar_tarefa.html'
    model = Tarefa
    context_object_name = 'tarefas'
    context = {}

    def get_success_url(self):
        return reverse_lazy('tarefas:tarefas')


class AtualizaUpdateView(UpdateView):
    model = Tarefa
    form_class = FormTarefa
    template_name = 'tarefas/atualiza.html'

    def get_success_url(self):
        return reverse_lazy('tarefas:tarefas')
