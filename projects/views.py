from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, AbonadoForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from projects.models import NewUser
from django.contrib.auth import authenticate, login, logout
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.tools as tls
import pandas as pd
from projects.models import Abonado, TRAFICO, Ingresos, AbonadosSten, IngresosSten, TraficoSten
from django.contrib import messages
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
            return redirect('User_welcome')
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
    
    select = request.GET.get('Table')
    Operator = request.GET.get('operador')

    if select == 'Abonados':
        Required_Table = Abonado.objects.all()
    elif select == 'Ingresos':
        Required_Table = Ingresos.objects.all()
    else:
        Required_Table = TRAFICO.objects.all()


    Tables = pd.DataFrame(list(Required_Table.values()))
    Tables = Tables.replace('', '0')
    cols = Tables.columns[Tables.columns.get_loc('mes'):Tables.columns.get_loc('suma_movil')+1]
    for col in cols:
        Tables[col] = Tables[col].astype('int64')

    Names = Tables.columns[3:17].values


    if Operator == 'colombia_telecomunicaciones':
        fig = px.line(x=Tables.id, 
                  y=Tables.colombia_telecomunicaciones, 
                  title='Trafico de Datos')
        fig.update_layout( 
                        xaxis = dict(
                            tickmode = 'array',
                            tickvals = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126],
                            ticktext = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
                        ))
        if select == 'Abonados':
            fig.update_layout(title='Abonados Colombia Telecomunicaciones')
        elif select == 'Ingresos':
            fig.update_layout(title='Ingresos Colombia Telecomunicaciones')
        elif select == 'Trafico':
            fig.update_layout(title='Trafico de Datos Colombia Telecomunicaciones')

    elif Operator == 'colombia_movil':
        fig = px.line(x=Tables.id, 
                  y=Tables.colombia_movil, 
                  title='Trafico de Datos')
        fig.update_layout(
                        xaxis = dict(
                            tickmode = 'array',
                            tickvals = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126],
                            ticktext = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
                        ))
        if select == 'Abonados':
            fig.update_layout(title='Abonados Colombia Movil')
        elif select == 'Ingresos':
            fig.update_layout(title='Ingresos Colombia Movil')
        elif select == 'Trafico':
            fig.update_layout(title='Trafico de Datos Colombia Movil')


    elif Operator == 'comunicacion_celular_comcel':
        fig = px.line(x=Tables.id, 
                  y=Tables.comunicacion_celular_comcel, 
                  title='Trafico de Datos')
        fig.update_layout(
                        xaxis = dict(
                            tickmode = 'array',
                            tickvals = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126],
                            ticktext = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
                        ))
        if select == 'Abonados':
            fig.update_layout(title='Abonados Comunicacion Celular Comcel')
        elif select == 'Ingresos':
            fig.update_layout(title='Ingresos Comunicacion Celular Comcel')
        elif select == 'Trafico':
            fig.update_layout(title='Trafico de Datos Comunicacion Celular Comcel')

    elif Operator == 'empresa_de_telecomunicaciones_de_bogota':
        fig = px.line(x=Tables.id, 
                  y=Tables.empresa_de_telecomunicaciones_de_bogota, 
                  title='Trafico de Datos')
        fig.update_layout(
                        xaxis = dict(
                            tickmode = 'array',
                            tickvals = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126],
                            ticktext = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
                        ))
        if select == 'Abonados':
            fig.update_layout(title='Abonados Empresa de Telecomunicaciones de Bogota')
        elif select == 'Ingresos':
            fig.update_layout(title='Ingresos Empresa de Telecomunicaciones de Bogota')
        elif select == 'Trafico':
            fig.update_layout(title='Trafico de Datos Empresa de Telecomunicaciones de Bogota')
    
    elif Operator == 'une_epm':
        fig = px.line(x=Tables.id, 
                  y=Tables.une_epm, 
                  title='Trafico de Datos')
        fig.update_layout( 
                        xaxis = dict(
                            tickmode = 'array',
                            tickvals = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126],
                            ticktext = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
                        ))
        if select == 'Abonados':
            fig.update_layout(title='Abonados UNE EPM')
        elif select == 'Ingresos':
            fig.update_layout(title='Ingresos UNE EPM')
        elif select == 'Trafico':
            fig.update_layout(title='Trafico de Datos UNE EPM')

    
    elif Operator == 'avantel':
        fig = px.line(x=Tables.id, 
                  y=Tables.avantel, 
                  title='Trafico de Datos')
        fig.update_layout(
                        xaxis = dict(
                            tickmode = 'array',
                            tickvals = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126],
                            ticktext = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
                        ))
        if select == 'Abonados':
            fig.update_layout(title='Abonados Avantel')
        elif select == 'Ingresos':
            fig.update_layout(title='Ingresos Avantel')
        elif select == 'Trafico':
            fig.update_layout(title='Trafico de Datos Avantel')

        
    elif Operator == 'almacenes_exito':
        fig = px.line(x=Tables.id, 
                  y=Tables.almacenes_exito, 
                  title='Trafico de Datos')
        fig.update_layout(
                        xaxis = dict(
                            tickmode = 'array',
                            tickvals = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126],
                            ticktext = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
                        ))
        if select == 'Abonados':
            fig.update_layout(title='Abonados Almacenes Exito')
        elif select == 'Ingresos':
            fig.update_layout(title='Ingresos Almacenes Exito')
        elif select == 'Trafico':
            fig.update_layout(title='Trafico de Datos Almacenes Exito')

        
    elif Operator == 'virgin_mobile':
        fig = px.line(x=Tables.id, 
                  y=Tables.virgin_mobile, 
                  title='Trafico de Datos')
        fig.update_layout(
                        xaxis = dict(
                            tickmode = 'array',
                            tickvals = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126],
                            ticktext = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
                        ))
        if select == 'Abonados':
            fig.update_layout(title='Abonados Virgin Mobile')
        elif select == 'Ingresos':
            fig.update_layout(title='Ingresos Virgin Mobile')
        elif select == 'Trafico':
            fig.update_layout(title='Trafico de Datos Virgin Mobile')


    elif Operator == 'partners_telecom':
        fig = px.line(x=Tables.id, 
                  y=Tables.partners_telecom, 
                  title='Trafico de Datos')
        fig.update_layout(
                        xaxis = dict(
                            tickmode = 'array',
                            tickvals = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126],
                            ticktext = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
                        ))
        if select == 'Abonados':
            fig.update_layout(title='Abonados Partners Telecom')
        elif select == 'Ingresos':
            fig.update_layout(title='Ingresos Partners Telecom')
        elif select == 'Trafico':
            fig.update_layout(title='Trafico de Datos Partners Telecom')

    
    elif Operator == 'setroc_mobile':
        fig = px.line(x=Tables.id, 
                  y=Tables.setroc_mobile, 
                  title='Trafico de Datos')
        fig.update_layout( 
                        xaxis = dict(
                            tickmode = 'array',
                            tickvals = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126],
                            ticktext = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
                        ))
        if select == 'Abonados':
            fig.update_layout(title='Abonados Setroc Mobile')
        elif select == 'Ingresos':
            fig.update_layout(title='Ingresos Setroc Mobile')
        elif select == 'Trafico':
            fig.update_layout(title='Trafico de Datos Setroc Mobile')

        
    elif Operator == 'uff_movil':
        fig = px.line(x=Tables.id, 
                  y=Tables.uff_movil, 
                  title='Trafico de Datos')
        fig.update_layout(
                        xaxis = dict(
                            tickmode = 'array',
                            tickvals = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126],
                            ticktext = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
                        ))
        if select == 'Abonados':
            fig.update_layout(title='Abonados UFF Movil')
        elif select == 'Ingresos':
            fig.update_layout(title='Ingresos UFF Movil')
        elif select == 'Trafico':
            fig.update_layout(title='Trafico de Datos UFF Movil')

        
    elif Operator == 'cellvoz_colombia':
        fig = px.line(x=Tables.id, 
                  y=Tables.cellvoz_colombia, 
                  title='Trafico de Datos')
        fig.update_layout( 
                        xaxis = dict(
                            tickmode = 'array',
                            tickvals = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126],
                            ticktext = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
                        ))
        if select == 'Abonados':
            fig.update_layout(title='Abonados Cellvoz Colombia')
        elif select == 'Ingresos':
            fig.update_layout(title='Ingresos Cellvoz Colombia')
        elif select == 'Trafico':
            fig.update_layout(title='Trafico de Datos Cellvoz Colombia')
        
    elif Operator == 'logistica_flash':
        fig = px.line(x=Tables.id, 
                  y=Tables.logistica_flash, 
                  title='Trafico de Datos')
        fig.update_layout(
                        xaxis = dict(
                            tickmode = 'array',
                            tickvals = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126],
                            ticktext = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
                        ))
        if select == 'Abonados':
            fig.update_layout(title='Abonados Logistica Flash')
        elif select == 'Ingresos':
            fig.update_layout(title='Ingresos Logistica Flash')
        elif select == 'Trafico':
            fig.update_layout(title='Trafico de Datos Logistica Flash')

        
    elif Operator == 'lov_telecomunicaciones':
        fig = px.line(x=Tables.id, 
                  y=Tables.lov_telecomunicaciones, 
                  title='Trafico de Datos')
        fig.update_layout( 
                        xaxis = dict(
                            tickmode = 'array',
                            tickvals = [6, 18, 30, 42, 54, 66, 78, 90, 102, 114, 126],
                            ticktext = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
                        ))
        if select == 'Abonados':
            fig.update_layout(title='Abonados LOV Telecomunicaciones')
        elif select == 'Ingresos':
            fig.update_layout(title='Ingresos LOV Telecomunicaciones')
        elif select == 'Trafico':
            fig.update_layout(title='Trafico de Datos LOV Telecomunicaciones')
    else:
        fig = px.line()

    figure = fig.to_html()
    


    context = {'figure': figure, 'names': Names}

    return render(request, "User_cargar_ingresos.html", context=context)

def grafico_tendencia(request):

    Table = request.GET.get('Table')
    Store_Table = Table
    fig = go.Figure()
    Required_Table = None


    if Table == 'Trafico':
        Required_Table = TraficoSten.objects.all()
    elif Table == 'Abonados':
        Required_Table = AbonadosSten.objects.all()
    else:
        Required_Table = IngresosSten.objects.all()
    
    #Abonados = Abonado.objects.all()
    if(Required_Table is not None):
        Annos = pd.DataFrame(list(Required_Table.values())).anno.unique()
    else:
        Annos = None
   
    start = request.GET.get('start')
    end = request.GET.get('end')

    if start or end:
        if start <= end:
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
    if Required_Table is not None:
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
        if Table == 'Trafico':
            fig.update_layout(title='Tendencia Trafico')
        elif Table == 'Abonados':
            fig.update_layout(title='Tendencia Abonados')
        else:
            fig.update_layout(title='Tendencia Ingresos')
    
    table = fig.to_html()
    context = {'table': table, 'form': AbonadoForm(), 'Required': Required_Table , 'Annos': Annos, 'Table': Store_Table}

    return render(request, "User_grafica_tendencia.html", context=context)

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
        Required_Table = Ingresos.objects.all()
    
    #Abonados = Abonado.objects.all()
    if(Required_Table is not None):
        Annos = pd.DataFrame(list(Required_Table.values())).anno.unique()
    else:
        Annos = None
   
    start = request.GET.get('start')
    end = request.GET.get('end')

    if start or end:
        if start <= end:
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
    if Required_Table is not None:
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
        if Table == 'Trafico':
            fig.update_layout(title='Historico Trafico de Datos')
            
        elif Table == 'Abonados':
            fig.update_layout(title='Historico Abonados')
        else:
            fig.update_layout(title='Historico Ingresos')
    
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