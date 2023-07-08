from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Producto, Usuario, ContactoGeneral

# fields = '__all__' | traigo todos los campos con esto
# widgets = {'fecha':forms.SelectDateWidget(years=range(1940,2023))} | para las fechas

class ProductoForm(ModelForm):
    class Meta:
        model   = Producto
        fields  = [
                    'id_producto', 
                    'id_artista', 
                    'nombre', 
                    'concepto', 
                    'tecnica', 
                    'precio', 
                    'descripcion', 
                    'imagen'
                  ] 
        

class RegistroForm(ModelForm):
    class Meta:
        model   = Usuario
        fields = '__all__'
        

class ContactoGeneralForm(ModelForm):
    class Meta:
        model   = ContactoGeneral 
        fields  = '__all__'