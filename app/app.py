from flask import Flask, flash, redirect, render_template, \
    request, url_for, session
from pickleshare import *
import ejercicios

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
          
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
    data_base = PickleShareDB('usuarios_db')

    if (request.method == 'POST'):
        usuario = request.form['usuario']
        password = request.form['password']

        # Si existe el usuario...
        if (usuario in data_base.keys()):

            # Si la contraseña del usuario coincide...
            if (password == data_base[usuario].get('password')):
                session['usuario'] = usuario
                session['password'] = password
                
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
    data_base = PickleShareDB('usuarios_db')

    if (request.method == 'POST'):
        usuario = request.form['usuario']
        password = request.form['password']

        # Si el usuario existe deberemos elegir otro
        if (usuario in data_base.keys()):
            error = 'Usuario existente, elige otro'
        # El usuario introducido no existe
        else:
            # Almacenamos usuario en la BD
            data_base[usuario] = {'password': password}
            
            # Establecemos la sesión, guardando el user y la pass
            session['usuario'] = usuario
            session['password'] = password
            
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

# A estemétodo le debe de llegar el POST y cambiar los datos.
@app.route('/modificar_datos')
def modificar_datos():
    usuario = password = ''
    
    if 'usuario' in session:
        usuario = session['usuario']

    if 'password' in session:
        password = session['password']

    return render_template('modificar_datos.html', usuario = usuario, password = password)

@app.route('/logout')
def logout():
    session.pop('usuario')
    session.pop('password')
    return redirect(url_for('index'))

@app.route('/interfaz_ejercicios/<ejercicio>')
def interfaz_ejercicios(ejercicio):
    return render_template('interfaz_ejercicios.html', ejercicio=ejercicio)
    

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

@app.errorhandler(404)
def page_not_found(error):
    return "<h1 style=\"color:red; text-align:center\";>Página no encontrada</h1>", 404