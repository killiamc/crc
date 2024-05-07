from django import forms
from django.contrib.auth.forms import UserCreationForm
from projects.models import NewUser

class CreateUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
            attrs={'placeholder': 'Contraseña', 'class': 'form-control', 'id': 'password1', 'required': 'required'}))
        
    password2 = forms.CharField(widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirmar contraseña', 'class': 'form-control', 'id': 'password2', 'required': 'required'}))
    
    class Meta:
        model = NewUser
        fields = ['first_name', 'last_name', 'email', 'telefono', 'cedula']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control', 'id': 'first_name', 'required': 'required'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Apellido', 'class': 'form-control', 'id': 'last_name', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'id': 'email', 'required': 'required'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Telefono', 'class': 'form-control', 'id': 'telefono', 'required': 'required'}),
            'cedula': forms.TextInput(attrs={'placeholder': 'Cedula', 'class': 'form-control', 'id': 'cedula', 'required': 'required'}),
        }





