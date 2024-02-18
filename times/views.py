from django.shortcuts import redirect, render
from times.forms import JogadoresForm
from times.models import Jogadores

# Create your views here.
def times(request):
    jogadores = Jogadores.objects.all()
    return render(request, 'index.html', {'jogadores': jogadores})

def create(request):
    if request.method == 'POST':
        form = JogadoresForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('times')
    else:
        form = JogadoresForm()
    return render(request, 'jogadores/create.html', {'form': form})

def update(request, id):
    jogador = Jogadores.objects.get(id=id)
    form = JogadoresForm(request.POST or None, instance=jogador)
    if form.is_valid():
        form.save()
        return redirect('times')
    return render(request, 'jogadores/update.html', {'form': form, 'jogador': jogador})

def delete(request, id):
    jogador = Jogadores.objects.get(id=id)
    jogador.delete()
    return redirect('times')
