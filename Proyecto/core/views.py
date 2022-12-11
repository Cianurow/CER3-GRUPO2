from distutils import core
from django import views
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Matrona
from .models import RecienNacido
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def sesionpadre(request):
    return render(request, 'core/sesionpadre.html')

def sesionmatrona(request):
    queryset = request.GET.get("usuario")
    queryset1 = request.GET.get("contraseña")
    matronas = Matrona.objects.all().order_by('run')
    if Matrona.objects.filter(run = queryset):
        if Matrona.objects.filter(contraseña = queryset1):
            matronas = Matrona.objects.filter(run = queryset) 
            return render(request, 'core/matrona.html', {'matronas':matronas})   
    return render(request, 'core/sesionmatrona.html')  

def padre(request):
    return render(request, 'core/padre.html')

@login_required
def matrona(request):
    reciennacido = RecienNacido.objects.all().order_by('fecha_nacimiento')
    return render(request, 'core/matrona.html', {'reciennacido':reciennacido})    



"""
def home(request):
    queryset = request.GET.get("buscar")
    correspondencias = Correspondencia.objects.all().order_by('nroResidencia')
    if queryset:
        if Correspondencia.objects.filter(nroResidencia = queryset):
            correspondencias = Correspondencia.objects.filter(nroResidencia = queryset)    
    
    return render(request, 'core/index.html', {'correspondencias':correspondencias})
"""