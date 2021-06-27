from django.shortcuts import redirect, render
from .forms import Alumno_form
from .models import alumno

# Create your views here.

def listar_alumnos(request):
    context = {'listar_alumnos' : alumno.objects.all()}
    return render(request, 'registro/listar_alumnos.html', context)

def form_alumnos(request, id=0):
    if request.method == "GET":
        if id == 0:
            form=Alumno_form()
        else:
            alumn = alumno.objects.get(pk=id)
            form = Alumno_form(instance = alumn)
        return render(request, 'registro/form_alumnos.html',{'form': form})
    else:
        if(id == 0):
            form = Alumno_form(request.POST)
        else:
            alumn = alumno.objects.get(pk=id)
            form = Alumno_form(request.POST, instance = alumn)
        if(form.is_valid()):
            form.save()
        return redirect('/alumnos/listar_alumnos')

def borrar_alumnos(request, id):
    alumn = alumno.objects.get(pk=id)
    alumn.delete()
    return redirect('/alumnos/listar_alumnos')
