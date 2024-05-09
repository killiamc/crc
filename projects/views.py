from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from projects.models import NewUser
from django.contrib.auth import authenticate, login, logout
import plotly.graph_objects as go
import pandas as pd


def ConfRegistro(request):
    return render(request, "ConfRegistro.html")

def Forget(request):
    return render(request, "Forget.html")

def Info(request):
    return render(request, "Info.html")

def Login(request):
    if request.method =="POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('grafico_tendencia')
        else:
            return redirect('Login')
    else:
        return render(request, "Login.html", {})

def Registro(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = True
            user.save()

            return redirect('Login')
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


    