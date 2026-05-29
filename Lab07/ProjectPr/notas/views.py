from django.shortcuts import render, redirect
from .forms import NotasForm
from .models import NotasAlumnosPorCurso

def guardar_notas(request):
    if request.method == 'POST':
        form = NotasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotasForm()
    return render(request, 'notas/guardar_notas.html', {'form': form})
def lista_notas(request):
    notas = NotasAlumnosPorCurso.objects.all()
    return render(request, 'notas/lista_notas.html', {'notas': notas})