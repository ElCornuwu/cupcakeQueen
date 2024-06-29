from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductoDeleteView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('logout/', views.exit, name='exit'),
    path('alfajores/', views.alfajores, name='alfajores'),
    path('base/', views.base, name='base'),
    path('cupcake/', views.cupcake, name='cupcake'),
    path('form/', views.form, name='form'),
    path('horario/', views.horario, name='horario'),
    path('productos/', views.productos, name='productos'),
    path('tortas/', views.tortas, name='tortas'),
    path('direccion/', views.direccion, name='direccion'),
    path('agregarProducto/', views.agregar_producto, name='agregarProducto'),
    path('eliminar/<int:producto_id>/', ProductoDeleteView.as_view(), name='eliminar_producto'),
    path('editar/<int:producto_id>/', views.editarProducto, name='editarProducto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)