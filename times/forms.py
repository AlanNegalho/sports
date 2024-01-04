from django.forms import ModelForm
from .models import Jogadores

class JogadoresForm(ModelForm):
    class Meta:
        model = Jogadores
        fields = ['nome', 'idade', 'posicao', 'numero', 'time', 'nacionalidade',]