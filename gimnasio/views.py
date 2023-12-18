from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ActividadForm, ProductoForm, ContactoForm
from .models import Actividad, Producto

def home(request):
    return render(request, 'gimnasio/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso.')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Cierre de sesión exitoso.')
        return redirect('home')
    return redirect('home')
@login_required
def agregar_actividad(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Actividad agregada exitosamente.')
            return redirect('home')
    else:
        form = ActividadForm()
    return render(request, 'agregar_actividad.html', {'form': form})

@login_required
def editar_actividad(request, actividad_id):
    actividad = Actividad.objects.get(pk=actividad_id)
    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            messages.success(request, 'Actividad editada exitosamente.')
            return redirect('home')
    else:
        form = ActividadForm(instance=actividad)
    return render(request, 'editar_actividad.html', {'form': form, 'actividad': actividad})

@login_required
def eliminar_actividad(request, actividad_id):
    actividad = Actividad.objects.get(pk=actividad_id)
    actividad.delete()
    messages.success(request, 'Actividad eliminada exitosamente.')
    return redirect('home')

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto agregado exitosamente.')
            return redirect('home')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

@login_required
def editar_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto editado exitosamente.')
            return redirect('home')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})

@login_required
def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    producto.delete()
    messages.success(request, 'Producto eliminado exitosamente.')
    return redirect('home')

@login_required
def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Mensaje enviado exitosamente.')
            return redirect('home')
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})

