from django import forms
from django.contrib.auth.forms import UserCreationForm
from projects.models import NewUser
from django.contrib.auth import get_user_model

User = get_user_model()

class CreateUserForm(forms.ModelForm):
    
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password', 'required': 'required'}))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'telefono', 'cedula']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control', 'id': 'first_name', 'required': 'required'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Apellido', 'class': 'form-control', 'id': 'last_name', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'id': 'email', 'required': 'required'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Telefono', 'class': 'form-control', 'id': 'telefono', 'required': 'required'}),
            'cedula': forms.TextInput(attrs={'placeholder': 'Cedula', 'class': 'form-control', 'id': 'cedula', 'required': 'required'}),
        }

    




