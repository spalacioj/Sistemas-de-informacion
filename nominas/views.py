from django.shortcuts import render, redirect
from nominas.empleados import Empleados
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm, LoginForm

# Create your views here.
@login_required
def index(request):
    empleados = []
    mensaje = ""
    try:
        empleados = Empleados.getEmpleados()
    except:
        mensaje = "Error en la base de datos"
    return render(request, 'nominas.html', {'mensaje': mensaje, 'empleados': empleados})

@login_required
def editarEmpleado(request, idEmpleado):
    empleado = Empleados.get_empleado_by_id(idEmpleado)
    info_empleado = empleado.get_info()
    if request.method == 'POST':
        Nombre = request.POST['nombre']
        Numero = request.POST['numero']
        Horas = request.POST['horas']
        actualizacion = Empleados.actualizar_empleado(idEmpleado, Nombre, Numero, Horas)
        return redirect('index')
    return render(request, 'editarEmpleados.html', {'empleado': info_empleado})

@login_required
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')