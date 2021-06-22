from AppProductos.models import Producto, Tipo
from django import forms
from django.db import models
from django.forms import ModelForm
from django.forms import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name','password1', 'password2']

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'tipo', 'precio', 'descripcion']

class TipoForm(ModelForm):
    class Meta:
        model = Tipo
        fields = ['nombre']