from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import logout
from .forms import ContactoForm, CustomUserCreationForm, ProductoForm
from django.contrib.auth import login
from .models import Producto, Categoria, Contacto
from django.views.generic import View
from django.contrib import messages

def superuser_required(user):
    return user.is_superuser

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
    productos = Producto.objects.all()
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

@user_passes_test(superuser_required)
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado correctamente.')
            return redirect('agregarProducto')  # Redirige a la misma página para limpiar el formulario
    else:
        form = ProductoForm()
    
    return render(request, 'agregarProducto.html', {'form': form})

@user_passes_test(superuser_required)
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

@user_passes_test(superuser_required)    
def editarProducto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')  
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'editarProducto.html', {'form': form, 'producto': producto})

def buscar_productos(request):
    query = request.GET.get('q', '')
    productos = Producto.objects.filter(nombre__icontains=query) if query else Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos, 'query': query})

def form(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Recibimos tu mensaje! Gracias por comunicarte.')
            return redirect('form')  
    else:
        form = ContactoForm()
    
    return render(request, 'form.html', {'form': form})

def mensajes(request):
    mensajes = Contacto.objects.all()
    context = {
        'mensajes': mensajes
    }
    return render(request, 'mensajes.html', context)