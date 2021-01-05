from django.shortcuts import render, HttpResponse
from .forms import NameForm

# Create your views here.

# Esta es la página controladora.

# Página de ejemplo para saber que funciona
def test_template(request):
    return HttpResponse('Hello World!')

# Renderizamos la página index
def index(request):
    return render(request, 'index.html')

def libros(request):
    return render(request, 'libros.html')

def prestamos(request):
    return render(request, 'prestamos.html')

def registro(request):
    return render(request, 'registro.html')

def login(request):
    return render(request, 'login.html')
