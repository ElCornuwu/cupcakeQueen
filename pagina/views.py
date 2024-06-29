from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

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
    return render(request, 'productos.html')

def tortas(request):
    return render(request, 'tortas.html')

