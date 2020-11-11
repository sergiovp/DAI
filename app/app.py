'''
Sergio Vela Pelegrina.

Desarrollo de Aplicaciones para Internet.

Ingeniería Informática UGR (2020/21).
'''

from flask import Flask, flash, redirect, render_template, \
    request, url_for, session
import ejercicios
import model

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

############################
# Práctica 1 y 2:
############################

@app.route('/ordena_burbuja/<numeros>')
def bubble_sort(numeros):
    # Quitamos las ','
    numeros = ejercicios.clean_list(numeros)

    # Añadimos un espacio al final del string
    numeros += ' '

    lista = []
    un_numero = ""

    for i in numeros:
        if (i != ' '):
            un_numero += i
        else:
            lista.append(int(un_numero))
            un_numero = ""

    lista = ejercicios.burbuja_sort(lista)

    return "El vector ordenado mediante burbuja: " + ''.join(str(lista))

@app.route('/ordena_seleccion/<numeros>')
def selection_sort(numeros):
    # Quitamos las ','
    numeros = ejercicios.clean_list(numeros)

    # Añadimos un espacio al final del string
    numeros += ' '

    lista = []
    un_numero = ""

    for i in numeros:
        if (i != ' '):
            un_numero += i
        else:
            lista.append(int(un_numero))
            un_numero = ""

    lista = ejercicios.seleccion_sort(lista)

    return "El vector ordenado mediante selección: " + ''.join(str(lista))

@app.route('/criba', methods=['GET'])
def criba(numero):
    primos = []
    primos = ejercicios.criba_eratostenes(numero)
    return "Los números primos hasta " + str(numero) + " son: " + ''.join(str(primos))

@app.route('/fibonacci/<int:numero>')
def fibonacci(numero):
    num_fibo = ejercicios.sucesion_fibonacci(numero)

    return "El número " + str(numero) + " ésimo de la sucesión de Fibonacci es: " + ''.join(str(num_fibo))

@app.route('/corchetes/<corchetes>')
def corchetes_balanceados(corchetes):
    mensaje = "' NO está balanceada"
    
    balanceada = ejercicios.is_balanceado(corchetes)

    if (balanceada):
        mensaje = "' SÍ está balanceada"

    return "La cadena '" + corchetes + mensaje

@app.route('/validar_correo/<correo>')
def validar_correo(correo):
    msg = "El correo '" + correo + "' NO es valido"
    valido = ejercicios.check_correo(correo)

    if (valido):
        msg = "El correo '" + correo + "' SÍ es valido"
    
    return msg

@app.route('/validar_tarjeta/<tarjeta>')
def validar_tarjeta(tarjeta):
    msg = "El número de tarjeta '" + tarjeta + "' NO es valido"
    valido = ejercicios.check_tarjeta(tarjeta)

    if (valido):
        msg = "El número de tarjeta '" + tarjeta + "' SÍ es valido"

    return msg

@app.route('/validar_palabra/<palabra>')
def validar_palabra(palabra):
    msg = "La palabra '" + palabra + "' NO es valida"
    valida = ejercicios.check_palabra(palabra)

    if (valida):
        msg = "La palabra '" + palabra + "' SÍ es valida"

    return msg

@app.route('/svg')
def svg():
    figura = ejercicios.crear_figura()
    return figura

############################
# Práctica 3:
############################

def start_session(usuario, password):
    session['usuario'] = usuario
    session['password'] = password

@app.route('/')
@app.route('/index')
def index():
    usuario = password = ''
    
    if 'usuario' in session:
        usuario = session['usuario']

    if 'password' in session:
        password = session['password']
    
    return render_template('index.html', usuario = usuario )

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    usuario = None

    if (request.method == 'POST'):
        usuario = request.form['usuario']
        password = request.form['password']

        # Si existe el usuario...
        if (model.check_key_exists(usuario)):

            # Si la contraseña del usuario coincide...
            if (model.check_password(usuario, password)):
                start_session(usuario, password)
                return render_template('index.html', usuario = usuario)
            # No coincide la contrasela...
            else:
                error = 'Contraseña incorrecta'
        # No existe el usuario
        else:
            error = 'El usuario no existe'

    return render_template('login.html', error = error)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    error = None

    if (request.method == 'POST'):
        usuario = request.form['usuario']
        password = request.form['password']

        # Si el usuario existe deberemos elegir otro
        if (model.check_key_exists(usuario)):
            error = 'Nombre de usuario en uso, elige otro.'
        # El usuario introducido no existe
        else:
            # Almacenamos usuario en la BD
            model.store_user(usuario, password)
            
            # Establecemos la sesión, guardando el user y la pass
            start_session(usuario, password)
            
            return render_template('index.html', usuario = usuario)

    return render_template('registro.html', error = error)

@app.route('/ver_datos')
def ver_datos():
    usuario = password = ''
    
    if 'usuario' in session:
        usuario = session['usuario']

    if 'password' in session:
        password = session['password']

    return render_template('ver_datos.html', usuario = usuario, password = password)

# A este método le debe de llegar el POST y cambiar los datos.
@app.route('/modificar_datos', methods=['GET', 'POST'])
def modificar_datos():
    #data_base = model.start_db()
    usuario = session['usuario']
    password = session['password']
    mensaje = 'Datos modificados correctamente'
    error = None

    # Hago las modificaciones oportunas
    if (request.method == 'POST'):

        if (request.form['usuario'] != session['usuario']):
            usuario = request.form['usuario']

            if (model.check_key_exists(usuario)):
                error = 'Nombre de usuario en uso, elige otro.'
                return render_template('modificar_datos.html', 
                usuario = session['usuario'], password = session['password'], error = error)

        if (request.form['password'] != session['password']):
            password = request.form['password']

        model.delete_user(session['usuario'])

        model.update_user_pass(usuario, password)
        session.clear()
        start_session(usuario, password)
        
        return render_template('modificar_datos.html',
        usuario = usuario, password = password, mensaje = mensaje)
    
    # Muestro los datos actuales
    else:
        render_template('modificar_datos.html', usuario = usuario, password = password)

        #if (usuario):
        #    data_base[session['usuario']] = usuario
    return render_template('modificar_datos.html', usuario = usuario, password = password)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/interfaz_ejercicios/<ejercicio>')
def interfaz_ejercicios(ejercicio):
    return render_template('interfaz_ejercicios.html', ejercicio=ejercicio)


@app.errorhandler(404)
def page_not_found(error):
    return "<h1 style=\"color:red; text-align:center\";>Página no encontrada</h1>", 404
