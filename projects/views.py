from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from projects.models import NewUser


def ConfRegistro(request):
    return render(request, "ConfRegistro.html")

def Forget(request):
    return render(request, "Forget.html")

def Info(request):
    return render(request, "Info.html")

def Login(request):
    return render(request, "Login.html")

def Registro(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ConfRegistro')
    else:
        print(form.errors)


    context = {'form': form}

    return render(request, "Registro.html", context=context) 

def ListaUsuarios(request):
    return render(request, "User_admin_listausuarios.html")

def permisos(request):
    return render(request, "User_admin_permisos.html")

def cargar_abonados(request):
    return render(request, "User_cargar_abonados.html")

def cargar_hist(request):
    return render(request, "User_cargar_hist.html")

def cargar_ingresos(request):
    return render(request, "User_cargar_ingresos.html")

def grafico_tendencia(request):
    return render(request, "User_grafica_tendencia.html")

def grafico_verhist(request):
    return render(request, "User_grafica_verhist.html")

def prepro_abonados(request):
    return render(request, "User_prepro_abonados.html")

def prepro_ingresos(request):
    return render(request, "User_prepro_ingresos.html")

def prepro_hist(request):
    return render(request, "User_prepro_hist.html")

def User_select(request):
    return render(request, "User_selection.html")


    