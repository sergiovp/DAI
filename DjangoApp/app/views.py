from django.shortcuts import render, HttpResponse
from .forms import *
from .models import *

# Create your views here.

# Esta es la página controladora.

usuario = ''

def check_session(request):
    return 'usuario' in request.session

def get_user_session(request):
    return request.session['usuario']

# Página de ejemplo para saber que funciona
def test_template(request):
    return HttpResponse('Hello World!')

# Renderizamos la página index
def index(request):
    global usuario

    if (check_session(request)):
        usuario = get_user_session(request)

    return render(request, 'index.html', {'usuario': usuario})

def libros(request):
    global usuario

    if (check_session(request)):
        usuario = get_user_session(request)

    libros = Libros.objects.all()

    return render(request, 'libros.html', {'libros': libros, 'usuario': usuario})

def add_libro(request):
    global usuario

    if (check_session(request)):
        usuario = get_user_session(request)

    if (request.method == 'POST'):
        form = add_libro_form(request.POST, request.FILES)

        if (form.is_valid()):
            form.save()
            libros = Libros.objects.all()
            return render(request, 'libros.html', {'libros': libros, 'usuario': usuario})

    else:
        form = add_libro_form()

    return render(request, 'libros_form.html', {'form': form})

def reservar_libro(request, identificador):
    global usuario

    if (check_session(request)):
        usuario = get_user_session(request)

    prestamo = Prestamos()
    libro = Libros()

    libro = Libros.objects.filter(id = identificador)

    Libros.objects.filter(id = identificador).update(
        reservado = True
    )

    prestamo.libro = Libros.objects.get(id = identificador)

    prestamo.usuario = usuario

    prestamo.save()
    libros = Libros.objects.all()

    return render(request, 'libros.html', {'libros': libros, 'usuario': usuario})

def modificar_libro(request, identificador):
    global usuario

    if (check_session(request)):
        usuario = get_user_session(request)

    libro = Libros.objects.filter(id = identificador)

    if (request.method == 'POST'):
        form = set_libro_form(request.POST, request.FILES)
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

                libros = Libros.objects.all()

                return render(request, 'libros.html', {'libros': libros, 'usuario': usuario})

    else:
        form = set_libro_form()

    return render(request, 'modificar_libro.html', {'form': form, 'libro': libro})

def eliminar_libro(request, identificador):
    global usuario

    if (check_session(request)):
        usuario = get_user_session(request)

    Libros.objects.filter(id = identificador).delete()

    libros = Libros.objects.all()

    return render(request, 'libros.html', {'libros': libros, 'usuario': usuario})

def eliminar_reserva(request, identificador_prestamo, identificador_libro):
    global usuario

    if (check_session(request)):
        usuario = get_user_session(request)

    prestamo = Prestamos()
    libro = Libros()

    Prestamos.objects.filter(id = identificador_prestamo).delete()

    Libros.objects.filter(id = identificador_libro).update(
        reservado = False
    )

    prestamo = Prestamos.objects.all()


    return render(request, 'prestamos.html', {'usuario': usuario, 'prestamos': prestamo})

def prestamos(request):
    global usuario

    if (check_session(request)):
        usuario = get_user_session(request)

    prestamos = Prestamos.objects.all()

    return render(request, 'prestamos.html', {'usuario': usuario, 'prestamos': prestamos})

def registro(request):
    error = ''

    if (request.method == 'POST'):
        form = registro_form(request.POST)

        if (form.is_valid()):
            user = Usuarios.objects.filter(usuario = request.POST.get('usuario'))
            if (user):
                error = 'Usuario en uso. Elige otro.'
            else:
                form.save()
                # Establecer sesión:
                request.session['usuario'] = request.POST.get('usuario')
                request.session['password'] = request.POST.get('password')

                return render(request, 'index.html', { 'usuario': request.session['usuario'] })

    else:
        form = registro_form()

    return render(request, 'registro.html', {'form': form, 'error': error})

def login(request):
    error = ''

    if (request.method == 'POST'):
        form = login_form(request.POST)

        if (form.is_valid()):

            # Comprobamos BD
            user = Usuarios.objects.filter(usuario = request.POST.get('usuario'))
            passw = Usuarios.objects.filter(password = request.POST.get('password'))

            # LogIn correcto
            if (user and passw):

                # Establecemos la sesión
                request.session['usuario'] = request.POST.get('usuario')
                request.session['password'] = request.POST.get('password')

                return render(request, 'index.html', {'usuario': request.session['usuario']})
            else:
                error = 'Usuario o contraseña incorrectos.'
    else:
        form = login_form()

    return render(request, 'login.html', { 'form': form, 'error': error })

# Deslogueo
def logout(request):
    global usuario

    usuario = ''

    # Eliminamos la sesión
    del request.session['usuario']
    del request.session['password']

    return render(request, 'index.html', {'usuario': ''})
