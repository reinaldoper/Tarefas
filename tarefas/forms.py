from django.core.exceptions import ValidationError
from django.forms import Form
from django.forms import CharField
from django.forms import EmailField
from django.forms import PasswordInput
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Tarefa


class FormTarefa(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'descricao', 'status']


