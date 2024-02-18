from django.forms import ModelForm
from .models import Jogadores, Times

class JogadoresForm(ModelForm):
    class Meta:
        model = Jogadores
        fields = ['nome', 'idade', 'posicao', 'numero', 'time', 'nacionalidade',]

class TimesForm(ModelForm):
    class Meta:
        model = Times
        fields = ['nome', 'tecnico', 'cidade', 'estado', 'pais',]