from django.shortcuts import render
from django.http import HttpResponse

def ConfRegistro(request):
    return render(request, "ConfRegistro.html")

def Forget(request):
    return render(request, "Forget.html")

def Info(request):
    return render(request, "Info.html")

def Login(request):
    return render(request, "Login.html")

def Registro(request):
    return render(request, "Registro.html")

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
    return render(request, "User_grafico_tendencia.html")

def grafico_verhist(request):
    return render(request, "User_grafico_verhist.html")

def prepro_abonados(request):
    return render(request, "User_prepro_abonados.html")

def prepro_ingresos(request):
    return render(request, "User_prepro_ingresos.html")

def prepro_hist(request):
    return render(request, "User_prepro_hist.html")

def User_select(request):
    return render(request, "User_selection.html")