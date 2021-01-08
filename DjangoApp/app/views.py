from django.shortcuts import render, HttpResponse
from .forms import *
from .models import *

# Create your views here.

# Esta es la página controladora.

usuario = ''

# Página de ejemplo para saber que funciona
def test_template(request):
    return HttpResponse('Hello World!')

# Renderizamos la página index
def index(request):
    return render(request, 'index.html', {'usuario': usuario})

def libros(request):
    libritos = ''

    libritos = Libros.objects.all()

    return render(request, 'libros.html', {'libros': libritos, 'usuario': usuario})

def add_libro(request):
    libritos = ''
    if (request.method == 'POST'):
        form = add_libro_form(request.POST)

        if (form.is_valid()):
            form.save()
            libritos = Libros.objects.all()
            return render(request, 'libros.html', {'libros': libritos, 'usuario': usuario})

    else:
        form = add_libro_form()

    return render(request, 'libros_form.html', {'form': form})

def reservar_libro(request, identificador):
    prestamo = Prestamos()
    libritos = ''
    libro = Libros()
    global usuario

    libro = Libros.objects.filter(id = identificador)

    Libros.objects.filter(id = identificador).update(
        reservado = True
    )

    prestamo.libro = Libros.objects.get(id = identificador)

    prestamo.usuario = usuario

    prestamo.save()
    libritos = Libros.objects.all()

    return render(request, 'libros.html', {'libros': libritos, 'usuario': usuario})

def modificar_libro(request, identificador):
    libro = Libros.objects.filter(id = identificador)
    print(libro)
    if (request.method == 'POST'):
        form = set_libro_form(request.POST)

        if (form.is_valid()):
            titulo = request.POST.get('titulo')
            autor = request.POST.get('autor')
            anio = request.POST.get('anio')

            if (titulo and autor and anio):
                Libros.objects.filter(id = identificador).update(
                    titulo = titulo,
                    autor = autor,
                    anio = anio
                )

                libritos = Libros.objects.all()
                print(titulo, autor, anio)
                return render(request, 'libros.html', {'libros': libritos, 'usuario': usuario})

    else:
        form = set_libro_form()

    return render(request, 'modificar_libro.html', {'form': form, 'libro': libro})

def eliminar_libro(request, identificador):
    libritos = ''
    Libros.objects.filter(id = identificador).delete()

    libritos = Libros.objects.all()

    return render(request, 'libros.html', {'libros': libritos, 'usuario': usuario})

def prestamos(request):
    prestamos = Prestamos.objects.all()
    return render(request, 'prestamos.html', {'usuario': usuario, 'prestamos': prestamos})

def registro(request):
    if (request.method == 'POST'):
        form = registro_form(request.POST)

        if (form.is_valid()):
            form.save()

            return render(request, 'index.html')

    else:
        form = registro_form()

    return render(request, 'registro.html', {'form': form})

def login(request):
    global usuario
    #return render(request, 'registro.html')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = login_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            usuario = titulo = request.POST.get('usuario')
            return render(request, 'index.html', {'usuario': usuario})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = login_form()

    return render(request, 'login.html', {'form': form, 'usuario': usuario})

def logout(request):
    global usuario

    usuario = ''

    return render(request, 'index.html', {'usuario': usuario})
