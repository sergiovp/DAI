from django.shortcuts import render, HttpResponse

# Create your views here.

# Esta es la página controladora.

# Página de ejemplo para saber que funciona
def test_template(request):
    return HttpResponse('Hello World!')

# Renderizamos la página index
def index(request):
    return render(request, 'index.html')

