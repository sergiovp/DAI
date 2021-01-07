from django.shortcuts import render, HttpResponse
from .forms import *
from .models import *

# Create your views here.

# Esta es la página controladora.

# Página de ejemplo para saber que funciona
def test_template(request):
    return HttpResponse('Hello World!')

# Renderizamos la página index
def index(request):
    return render(request, 'index.html')

def libros(request):
    libritos = ''

    libritos = Libros.objects.all()

    return render(request, 'libros.html', {'libros': libritos})

def add_libro(request):
    libritos = ''
    if (request.method == 'POST'):
        form = add_libro_form(request.POST)

        if (form.is_valid()):
            form.save()
            libritos = Libros.objects.all()
            return render(request, 'libros.html', {'libros': libritos})

    else:
        form = add_libro_form()

    return render(request, 'libros_form.html', {'form': form})
    #return HttpResponse('Hello World!')

def eliminar_libro(request, identificador):
    libritos = ''
    Libros.objects.filter(id = identificador).delete()

    libritos = Libros.objects.all()

    return render(request, 'libros.html', {'libros': libritos})

def prestamos(request):
    return render(request, 'prestamos.html')

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
    #return render(request, 'registro.html')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = login_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return 'HELLO'

    # if a GET (or any other method) we'll create a blank form
    else:
        form = login_form()

    return render(request, 'login.html', {'form': form})

    