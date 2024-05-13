from django.urls import path
from . import views

urlpatterns = [
    path('', views.Info, name='Info'),
    path('Login/', views.Login, name='Login'),
    path('Registro/', views.Registro, name='Registro'),
    path('ConfRegistro/', views.ConfRegistro, name='ConfRegistro'),
    path('Forget/', views.Forget, name='Forget'),
    path('ListaUsuarios/', views.ListaUsuarios, name='ListaUsuarios'),
    path('permisos/', views.permisos, name='permisos'),
    path('cargar_abonados/', views.cargar_abonados, name='cargar_abonados'),
    path('cargar_hist/', views.cargar_hist, name='cargar_hist'),
    path('cargar_ingresos/', views.cargar_ingresos, name='cargar_ingresos'),
    path('grafico_tendencia/', views.grafico_tendencia, name='grafico_tendencia'),
    path('grafico_verhist/', views.grafico_verhist, name='grafico_verhist'),
    path('prepro_abonados/', views.prepro_abonados, name='prepro_abonados'),
    path('prepro_ingresos/', views.prepro_ingresos, name='prepro_ingresos'),
    path('prepro_hist/', views.prepro_hist, name='prepro_hist'),
    path('User_select/', views.User_select, name='User_select'),
    path('User_welcome/', views.User_welcome, name='User_welcome'),
    path('admin/', views.go_to_admin, name='admin'),
    path('logout/', views.logout_view, name='logout')
]