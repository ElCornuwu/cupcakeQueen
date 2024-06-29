from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm, ProductoForm
from django.contrib.auth import authenticate, login
from .models import Producto, Categoria
from django.views.generic import View
# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def exit(request):
    logout(request)
    return redirect(index)

def base(request):
    return render(request, 'base.html')

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
    categoria_torta = Categoria.objects.get(nombre="Torta")
    productos = Producto.objects.filter(categoria=categoria_torta)
    
    return render(request, 'tortas.html', {'productos': productos})

def alfajores(request):
    categoria_Alfajor = Categoria.objects.get(nombre="Alfajor")
    productos = Producto.objects.filter(categoria=categoria_Alfajor)
    
    return render(request, 'alfajores.html', {'productos': productos})

def cupcake(request):
    categoria_Cupcake = Categoria.objects.get(nombre="Cupcake")
    productos = Producto.objects.filter(categoria=categoria_Cupcake)
    
    return render(request, 'cupcake.html', {'productos': productos})

def direccion(request):
    return render(request, 'direccion.html')    

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
    
def editarProducto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')  # Redirige a la lista de productos después de guardar
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'editarProducto.html', {'form': form, 'producto': producto})