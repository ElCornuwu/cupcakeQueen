from django.shortcuts import render
# Create your views here.

def pagInicio(request):
    return render(request, 'index.html')

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

def login(request):
    return render(request, 'login.html')

def productos(request):
    return render(request, 'productos.html')

def tortas(request):
    return render(request, 'tortas.html')