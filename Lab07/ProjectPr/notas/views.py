from django.shortcuts import render, redirect
from .forms import NotasForm
from .models import NotasAlumnosPorCurso

def crear_venta(request):
    if request.method == 'POST':
        form = NotasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotasForm()
    return render(request, 'notas/crear_venta.html', {'form': form})
def lista_notas(request):
    notas = NotasAlumnosPorCurso.objects.all()
    return render(request, 'notas/lista_notas.html', {'notas': notas})