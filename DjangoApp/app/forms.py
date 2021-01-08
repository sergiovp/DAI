from django import forms
from .models import *
from django.contrib.auth.models import User

class registro_form(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget = forms.PasswordInput)
        model = User
        widgets = {'password': forms.PasswordInput()}
        fields = ('username', 'password',)
        help_texts = {
            'username': None,
        }

class login_form(forms.Form):
    usuario = forms.CharField(label='Usuario', max_length=100)
    password = forms.CharField(widget = forms.PasswordInput, label='Contraseña')

class add_libro_form(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ('titulo', 'autor', 'anio',)

class set_libro_form(forms.ModelForm):
    class Meta:
        model = Libros
        fields = ('titulo', 'autor', 'anio',)
