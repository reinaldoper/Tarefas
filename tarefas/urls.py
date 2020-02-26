from django.urls import path
from .views import Home, AdicionaTarefa, DeleteTarefa, AtualizaUpdateView
from .views import TarefasView, TarefaDetail

app_name = 'tarefas'
urlpatterns = [
    path('', Home.as_view()),
    path('tarefas/', TarefasView.as_view(), name='tarefas'),
    path('tarefas/<int:pk>/', TarefaDetail.as_view()),
    path('tarefas/criar/', AdicionaTarefa.as_view()),
    path('tarefas/excluir/<int:pk>/', DeleteTarefa.as_view()),
    path('tarefas/atualiza/<int:pk>/', AtualizaUpdateView.as_view()),
]
