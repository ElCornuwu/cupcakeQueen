from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('logout/', views.exit, name='exit'),
    path('alfajores/', views.alfajores, name='alfajores'),
    path('base/', views.base, name='base'),
    path('cupcake/', views.cupcake, name='cupcake'),
    path('form/', views.form, name='form'),
    path('horario/', views.horario, name='horario'),
    path('productos/', views.productos, name='productos'),
    path('tortas/', views.tortas, name='tortas'),
    path('direccion/', views.direccion, name='direccion'),
]