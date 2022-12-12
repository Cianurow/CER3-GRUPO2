"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from core import views
from core.api.router import router_seguimiento


urlpatterns = [
        
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('sesionpadre/', views.sesionpadre, name="sesionpadre"),
    path('sesionmatrona/', views.sesionmatrona, name="sesionmatrona"),
    path('padre/', views.padre, name="padre"),
    path('matrona/', views.matrona, name="matrona"),
    path('seguimiento/<int:id>', views.seguimiento, name="seguimiento"),
    path('seguimientopadre/<int:id>', views.seguimientopadre, name="seguimientopadre"),
    path('alta/', views.alta, name="alta"),
    path('api/',include(router_seguimiento.urls), name="api"),

]
