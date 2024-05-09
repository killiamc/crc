from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, AbonadoForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from projects.models import NewUser
from django.contrib.auth import authenticate, login, logout
import plotly.graph_objects as go
import pandas as pd
from projects.models import Abonado, TRAFICO
from django. contrib import messages

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
    
    Table = request.GET.get('Table')
    Store_Table = Table
    fig = go.Figure()
    Required_Table = None


    if Table == 'Trafico':
        Required_Table = TRAFICO.objects.all()
    elif Table == 'Abonados':
        Required_Table = Abonado.objects.all()
    else:
        pass
    
    #Abonados = Abonado.objects.all()
    if(Required_Table is not None):
        Annos = pd.DataFrame(list(Required_Table.values())).anno.unique()
    else:
        Annos = None
   
    start = request.GET.get('start')
    end = request.GET.get('end')

    if start or end:
        if start < end:
            if start:
                if start == 'start':
                    messages.error(request, 'Por favor ingrese una fecha de inicio')
                else:
                    print(start)
                    Required_Table = Required_Table.filter(anno__gte=start)
            if end:
                if end == 'end':
                    messages.error(request, 'Por favor ingrese una fecha de fin')
                else:
                    print(end)
                    Required_Table = Required_Table.filter(anno__lte=end)
    
    if Required_Table is not None:
        Abon = pd.DataFrame(list(Required_Table.values()))
    #print(Abon)
    if Table == 'Abonados':
        fig = go.Figure(data=[go.Table(
        header=dict(values=['Año', 'Mes', 'Colombia Telecom', 'Colombia Movil', 'Comcel', 'ETB', 'UNE EPM', 'Avantel', 'Exito', 'Virgin Mobile', 'Partners Telecom', 'Setroc Mobile', 'UFF Movil', 'Cellvoz Colombia', 'Logistica Flash', 'LOV Telecom', 'Suma Movil']),
        cells=dict(values=[Abon.anno, 
                           Abon.mes, 
                           Abon.colombia_telecomunicaciones, 
                           Abon.colombia_movil, 
                           Abon.comunicacion_celular_comcel, 
                           Abon.empresa_de_telecomunicaciones_de_bogota, 
                           Abon.une_epm, Abon.avantel, 
                           Abon.almacenes_exito, 
                           Abon.virgin_mobile, 
                           Abon.partners_telecom, 
                           Abon.setroc_mobile, 
                           Abon.uff_movil, 
                           Abon.cellvoz_colombia, 
                           Abon.logistica_flash, 
                           Abon.lov_telecomunicaciones, 
                           Abon.suma_movil],
                     align='center',
                     fill_color = 'lightgrey',
                     alignsrc = 'center',
                    )),
        ])
        fig.update_layout(title_text='Historico de Abonados')
    elif Table == 'Trafico':
        #ANNO,MES,COLOMBIA_TELECOMUNICACIONES,COLOMBIA_MOVIL,COMUNICACION_CELULAR_COMCEL,EMPRESA_DE_TELECOMUNICACIONES_DE_BOGOTA,UNE_EPM,AVANTEL,ALMACENES_EXITO,VIRGIN_MOBILE,PARTNERS_TELECOM,SETROC_MOBILE,UFF_MOVIL,CELLVOZ_COLOMBIA,LOGISTICA_FLASH,LOV_TELECOMUNICACIONES,SUMA_MOVIL
        print('Entro')
        fig = go.Figure(data=[go.Table(
        header=dict(values=['Año', 'Mes', 'Colombia Telecom', 'Colombia Movil', 'Comcel', 'ETB', 'UNE EPM', 'Avantel', 'Exito', 'Virgin Mobile', 'Partners Telecom', 'Setroc Mobile', 'UFF Movil', 'Cellvoz Colombia', 'Logistica Flash', 'LOV Telecom', 'Suma Movil']),
        cells=dict(values=[Abon.anno, 
                           Abon.mes, 
                           Abon.colombia_telecomunicaciones, 
                           Abon.colombia_movil, 
                           Abon.comunicacion_celular_comcel, 
                           Abon.empresa_de_telecomunicaciones_de_bogota, 
                           Abon.une_epm, Abon.avantel, 
                           Abon.almacenes_exito, 
                           Abon.virgin_mobile, 
                           Abon.partners_telecom, 
                           Abon.setroc_mobile, 
                           Abon.uff_movil, 
                           Abon.cellvoz_colombia, 
                           Abon.logistica_flash, 
                           Abon.lov_telecomunicaciones, 
                           Abon.suma_movil],
                     align='center',
                     fill_color = 'lightgrey',
                     alignsrc = 'center',
                    )),
        ])
        fig.update_layout(title_text='Historico de Traficos')

    table = fig.to_html()
    context = {'table': table, 'form': AbonadoForm(), 'Required': Required_Table , 'Annos': Annos, 'Table': Store_Table}

    return render(request, "User_grafica_verhist.html", context=context)
    


def prepro_abonados(request):
    return render(request, "User_prepro_abonados.html")

def prepro_ingresos(request):
    return render(request, "User_prepro_ingresos.html")

def prepro_hist(request):
    return render(request, "User_prepro_hist.html")

def User_select(request):
    return render(request, "User_selection.html")

def User_welcome(request):
    return render(request, "User_welcome.html")