from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.

class CustomAccountManager(BaseUserManager):

    def create_user(self, first_name, last_name, email, password, telefono, cedula, **other_fields):
        
        

        if not email:
            raise ValueError('El email es obligatorio')
        
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            telefono=telefono,
            cedula=cedula,
            **other_fields
        )
        
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, email, password, telefono, cedula, **other_fields):
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True')


        return self.create_user(first_name, last_name, email, password, telefono, cedula, **other_fields)


class NewUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=100)
    cedula = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'telefono', 'cedula']

    def __str__(self):
        return self.email
    
class TRAFICO(models.Model):
    #ANNO,MES,COLOMBIA_TELECOMUNICACIONES,COLOMBIA_MOVIL,COMUNICACION_CELULAR_COMCEL,EMPRESA_DE_TELECOMUNICACIONES_DE_BOGOTA,UNE_EPM,AVANTEL,ALMACENES_EXITO,VIRGIN_MOBILE,PARTNERS_TELECOM,SETROC_MOBILE,UFF_MOVIL,CELLVOZ_COLOMBIA,LOGISTICA_FLASH,LOV_TELECOMUNICACIONES,SUMA_MOVIL
    anno = models.CharField(max_length=100)
    mes = models.CharField(max_length=100)
    colombia_telecomunicaciones = models.CharField(max_length=100)
    colombia_movil = models.CharField(max_length=100)
    comunicacion_celular_comcel = models.CharField(max_length=100)
    empresa_de_telecomunicaciones_de_bogota = models.CharField(max_length=100)
    une_epm = models.CharField(max_length=100)
    avantel = models.CharField(max_length=100)
    almacenes_exito = models.CharField(max_length=100)
    virgin_mobile = models.CharField(max_length=100)
    partners_telecom = models.CharField(max_length=100)
    setroc_mobile = models.CharField(max_length=100)
    uff_movil = models.CharField(max_length=100)
    cellvoz_colombia = models.CharField(max_length=100)
    logistica_flash = models.CharField(max_length=100)
    lov_telecomunicaciones = models.CharField(max_length=100)
    suma_movil = models.CharField(max_length=100)


    class Meta:
        ordering = ['anno']

    def __str__(self):
        return self.nombre
    
class Abonado(models.Model):
    #,ANNO,MES,COLOMBIA_TELECOMUNICACIONES,COLOMBIA_MOVIL,COMUNICACION_CELULAR_COMCEL,EMPRESA_DE_TELECOMUNICACIONES_DE_BOGOTA,UNE_EPM,AVANTEL,ALMACENES_EXITO,VIRGIN_MOBILE,PARTNERS_TELECOM,SETROC_MOBILE,UFF_MOVIL,CELLVOZ_COLOMBIA,LOGISTICA_FLASH,LOV_TELECOMUNICACIONES,SUMA_MOVIL
    anno = models.CharField(max_length=100)
    mes = models.CharField(max_length=100)
    colombia_telecomunicaciones = models.CharField(max_length=100)
    colombia_movil = models.CharField(max_length=100)
    comunicacion_celular_comcel = models.CharField(max_length=100)
    empresa_de_telecomunicaciones_de_bogota = models.CharField(max_length=100)
    une_epm = models.CharField(max_length=100)
    avantel = models.CharField(max_length=100)
    almacenes_exito = models.CharField(max_length=100)
    virgin_mobile = models.CharField(max_length=100)
    partners_telecom = models.CharField(max_length=100)
    setroc_mobile = models.CharField(max_length=100)
    uff_movil = models.CharField(max_length=100)
    cellvoz_colombia = models.CharField(max_length=100)
    logistica_flash = models.CharField(max_length=100)
    lov_telecomunicaciones = models.CharField(max_length=100)
    suma_movil = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['anno']


    