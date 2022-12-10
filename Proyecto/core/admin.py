from django.contrib import admin
from .models import Seguimiento,Padre,Matrona,Usuario,RecienNacido

admin.site.register(Seguimiento)
admin.site.register(Padre)
admin.site.register(Usuario)
admin.site.register(RecienNacido)
admin.site.register(Matrona)
