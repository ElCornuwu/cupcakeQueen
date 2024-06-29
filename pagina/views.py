from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from .forms import ProductoForm
from .models import Producto
from django.views.generic import View

# Create your views here.

def index(request):
    return render(request, 'index.html')

def exit(request):
    logout(request)
    return redirect(index)

def alfajores(request):
    return render(request, 'alfajores.html')

def base(request):
    return render(request, 'base.html')

def cupcake(request):
    return render(request, 'cupcake.html')

def form(request):
    return render(request, 'form.html')

def horario(request):
    return render(request, 'horario.html')

def productos(request):
    productos = Producto.objects.all()  # Obtener todos los productos
    context = {
        'productos': productos
    }
    return render(request, 'productos.html', context)

def tortas(request):
    return render(request, 'tortas.html')

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('agregarProducto')  # Redirige a donde desees tras guardar el producto
    else:
        form = ProductoForm()
    
    return render(request, 'agregarProducto.html', {'form': form})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')
    
    return render(request, 'eliminar_producto.html', {'producto': producto})

class ProductoDeleteView(View):
    def get(self, request, producto_id):
        producto = get_object_or_404(Producto, pk=producto_id)
        return render(request, 'eliminar_producto.html', {'producto': producto})

    def post(self, request, producto_id):
        producto = get_object_or_404(Producto, pk=producto_id)
        producto.delete()
        return redirect('productos')
