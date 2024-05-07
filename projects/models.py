from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.

class CustomAccountManager(BaseUserManager):

    def create_user(self, first_name, last_name, email, password, telefono, cedula, **other_fields):
        
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)

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
        user.save(using=self._db)
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
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'telefono', 'cedula', 'password']

    class Meta:
        verbose_name = 'email'
        verbose_name_plural = 'emails'

    def __str__(self):
        return self.email