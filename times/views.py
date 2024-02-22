from django.shortcuts import redirect, render
from times.forms import JogadoresForm, TimesForm
from times.models import Jogadores, Times

# Create your views here.
def atletas(request):
    jogadores = Jogadores.objects.all()
    times = Times.objects.all()
    return render(request, 'index.html', {'jogadores': jogadores, 'times': times})

def jogador(request):
    jogadores = Jogadores.objects.all()
    return render(request, 'jogadores/jogadores.html', {'jogadores': jogadores})

def create(request):
    if request.method == 'POST':
        form = JogadoresForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('atletas')
    else:
        form = JogadoresForm()
    return render(request, 'jogadores/create.html', {'form': form})

def update(request, id):
    jogador = Jogadores.objects.get(id=id)
    form = JogadoresForm(request.POST or None, instance=jogador)
    if form.is_valid():
        form.save()
        return redirect('atletas')
    return render(request, 'jogadores/update.html', {'form': form, 'jogador': jogador})

def delete(request, id):
    jogador = Jogadores.objects.get(id=id)
    jogador.delete()
    return redirect('atletas')

# Times

def times (request):
    times = Times.objects.all()
    return render(request, 'time/times.html', {'times': times})

def create_time(request):
    if request.method == 'POST':
        form = TimesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('times')
    else:
        form = TimesForm()
    return render(request, 'time/creat_time.html', {'form': form})

def update_time(request, id):
    times = Times.objects.get(id=id)
    form = TimesForm(request.POST or None, instance=times)
    if form.is_valid():
        form.save()
        return redirect('times')
    return render(request, 'time/update_time.html', {'form': form, 'times': times})

def delete_time(request, id):
    times = Times.objects.get(id = id)
    times.delete()
    return redirect('times')
