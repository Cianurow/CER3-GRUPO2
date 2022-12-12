from distutils import core
from django import views
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Matrona
from .models import RecienNacido
from .models import Padre
from .models import Seguimiento
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def sesionpadre(request):
    queryset = request.GET.get("usuario")
    queryset1 = request.GET.get("contraseña")
    padres = Padre.objects.all()
    if Padre.objects.filter(run = queryset):
        if Padre.objects.filter(contraseña = queryset1):
            padres = Padre.objects.filter(run = queryset) 
            return padre(request, padres)
    return render(request, 'core/sesionpadre.html')

def sesionmatrona(request):
    queryset = request.GET.get("usuario")
    queryset1 = request.GET.get("contraseña")
    matronas = Matrona.objects.all().order_by('run')
    if Matrona.objects.filter(run = queryset):
        if Matrona.objects.filter(contraseña = queryset1):
            matronas = Matrona.objects.filter(run = queryset) 
            return matrona(request)    
    return render(request, 'core/sesionmatrona.html')  

@login_required
def matrona(request):
    reciennacido = RecienNacido.objects.all().order_by('fecha_nacimiento')
    seguimientos = Seguimiento.objects.all()
    return render(request, 'core/matrona.html', {'reciennacido':reciennacido, 'seguimientos':seguimientos})    

@login_required
def alta(request):
    reciennacido = RecienNacido.objects.all().order_by('fecha_nacimiento')
    seguimientos = Seguimiento.objects.all()
    return render(request, 'core/alta.html', {'reciennacido':reciennacido, 'seguimientos':seguimientos})   


@login_required
def padre(request, padres):
    for padre in padres:
        if RecienNacido.objects.filter(padres = padre):
            reciennacido = RecienNacido.objects.filter(padres = padre)
    return render(request, 'core/padre.html', {'reciennacido':reciennacido, 'padres':padres})  



@login_required
def seguimiento (request, id):

    seguimientos = Seguimiento.objects.all()
    reciennacido = RecienNacido.objects.filter(id = id)
    if id:

        seguimientos = Seguimiento.objects.filter(recien_nacido = id)
        return render(request, 'core/seguimiento.html', {'seguimientos':seguimientos})

   
    return render(request, 'core/seguimiento.html', {'seguimientos':seguimientos})

@login_required
def seguimientopadre (request, id):

    seguimientos = Seguimiento.objects.all()
    reciennacido = RecienNacido.objects.filter(id = id)
    if id:

        seguimientos = Seguimiento.objects.filter(recien_nacido = id)
        return render(request, 'core/seguimiento.html', {'seguimientos':seguimientos})
    return render(request, 'core/seguimiento.html', {'seguimientos':seguimientos})    
