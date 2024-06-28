"""
URL configuration for cupcakeQueen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from pagina import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagInicio, name='index'),
    path('alfajores/', views.alfajores, name='alfajores'),
    path('base/', views.base, name='base'),
    path('cupcake/', views.cupcake, name='cupcake'),
    path('form/', views.form, name='form'),
    path('horario/', views.horario, name='horario'),
    path('login/', views.login, name='login'),
    path('productos/', views.productos, name='productos'),
    path('tortas/', views.tortas, name='tortas'),
]
