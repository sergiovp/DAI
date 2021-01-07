from django import forms
from .models import *

class registro_form(forms.ModelForm):
    class Meta:
        model = usuarios
        password = forms.CharField(widget = forms.PasswordInput)
        widgets = {'password': forms.PasswordInput()}
        fields = ('usuario', 'password',)

class login_form(forms.Form):
    usuario = forms.CharField(label='Usuario', max_length=100)
    password = forms.CharField(widget = forms.PasswordInput, label='Contraseña')

class add_libro_form(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ('titulo', 'autor', 'anio',)
