from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test_template', views.test_template, name='test_template'),
    path('libros', views.libros, name='libros'),
    path('prestamos', views.prestamos, name='prestamos'),
    path('registro', views.registro, name='registro'),
    path('login', views.login, name='login'),
    path('add_libro', views.add_libro, name='add_libro'),
    path('eliminar_libro/<int:identificador>', views.eliminar_libro, name='eliminar_libro'),
    path('modificar_libro/<int:identificador>', views.modificar_libro, name='modificar_libro'),
    path('logout', views.logout, name='logout'),
    path('reservar_libro/<int:identificador>', views.reservar_libro, name='reservar_libro'),
]
