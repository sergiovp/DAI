'''
Sergio Vela Pelegrina.

Desarrollo de Aplicaciones para Internet.

Ingeniería Informática UGR (2020/21).
'''

from flask import Flask, flash, redirect, render_template, \
    request, url_for, session
import ejercicios
import model
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Start MongoDB and load our DB
client = MongoClient("mongo", 27017)
db = client.SampleCollections

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

@app.route('/criba/<numero>')
def criba(numero):
    primos = []
    primos = ejercicios.criba_eratostenes(int(numero))
    return "Los números primos hasta " + str(numero) + " son: " + ''.join(str(primos))

@app.route('/fibonacci/<numero>')
def fibonacci(numero):
    num_fibo = ejercicios.sucesion_fibonacci(int(numero))

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
    #return '<h1>Hola</h1>'

############################
# Práctica 3:
############################

# Diccionario global. Almacenará la URL y nombre con el que quiero que aparezca.
paginas = {}

def update_paginas(url, nombre):
    if (len(paginas) >= 3):
        if (not url in paginas):
            del paginas[next(iter(paginas))]
            paginas.update({url: nombre})
    else:
        paginas.update({url: nombre})

def start_session(usuario, password):
    session['usuario'] = usuario
    session['password'] = password

def get_user_session():
    if ('usuario' in session):
        return session['usuario']
    else: return

def get_pass_session():
    if ('password' in session):
        return session['password']
    else: return

@app.route('/')
@app.route('/index')
def index():
    # Comprobamos si se ha iniciado la sesión
    usuario = get_user_session()
    password = get_pass_session()
    
    return render_template('index.html', usuario = usuario, paginas = paginas)

@app.route('/login', methods=['GET', 'POST'])
def login():
    usuario = error = None

    update_paginas('login', 'LogIn')

    if (request.method == 'POST'):
        usuario = request.form['usuario']
        password = request.form['password']

        # Si existe el usuario...
        if (model.check_key_exists(usuario)):

            # Si la contraseña del usuario coincide...
            if (model.check_password(usuario, password)):
                # EN ESTE PUNTO COMENZAMOS LA SESIÓN
                start_session(usuario, password)

                return render_template('index.html', usuario = usuario, paginas = paginas)
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

    update_paginas('registro', 'Regístrate')

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
    # Lo comprobamos por si alguien intenta acceder a la URL sin estar logeado
    usuario = get_user_session()
    password = get_pass_session()

    update_paginas('ver_datos', 'Mis datos')

    return render_template('ver_datos.html', 
        usuario = usuario, password = password)

@app.route('/modificar_datos', methods=['GET', 'POST'])
def modificar_datos():
    # Lo comprobamos por si alguien intenta acceder a la URL sin estar logeado
    usuario = get_user_session()
    password = get_pass_session()

    mensaje = 'Datos modificados correctamente'
    error = None

    update_paginas('modificar_datos', 'Modificar datos')

    # Si introducimos datos en el formulario
    if (request.method == 'POST'):

        # Si han modificado el nombre de usuario
        if ((request.form['usuario'] != usuario) and request.form['usuario']):
            usuario = request.form['usuario']

            # Si el nombre nuevo ya está cogido por otro
            if (model.check_key_exists(usuario)):
                error = 'Nombre de usuario en uso, elige otro.'
                
                return render_template('modificar_datos.html', usuario = usuario, 
                    password = password, error = error)

        # Si han modificado la contraseña
        if ((request.form['password'] != password) and request.form['password']):
            password = request.form['password']

        # Borramos de la BD el usuario con nombre antiguo
        model.delete_user(session['usuario'])

        # Actualizamos de la BD el usuario y pass
        model.update_user_pass(usuario, password)

        # Eliminamos y volvemos a establecer la sesión con los datos actualizados
        session.clear()
        start_session(usuario, password)
        
        return render_template('modificar_datos.html',
            usuario = usuario, password = password, mensaje = mensaje)

    return render_template('modificar_datos.html', usuario = usuario, password = password)

@app.route('/logout')
def logout():
    session.clear()
    paginas.clear()
    return redirect(url_for('index'))

@app.route('/interfaz_ejercicios/<nombre>/<ejercicio>', methods=['GET', 'POST'])
def interfaz_ejercicios(nombre, ejercicio):
    parametros = mensaje = ''
    usuario = get_user_session()

    '''
        Como parámetro recibimos el nombre que queremos que aparezca en el menú (nombre)
        y el nombre de la función para el enlace (ejercicio)

        parametros será la variable por si introducimos datos en el formulario de los ejercicios

        mensaje será lo que devolveremos como resultado de los ejercicios
    '''

    if (request.method == 'POST'):
        parametros = request.form['param-ejercicio']
        if (parametros):
            if (ejercicio == 'burbuja'):
                mensaje = bubble_sort(parametros)
            elif (ejercicio == 'seleccion'):
                mensaje = selection_sort(parametros)
            elif (ejercicio == 'criba'):
                mensaje = criba(parametros)
            elif (ejercicio == 'fibonacci'):
                mensaje = fibonacci(parametros)
            elif (ejercicio == 'corchetes'):
                mensaje = corchetes_balanceados(parametros)
            elif (ejercicio == 'correo'):
                mensaje = validar_correo(parametros)
            elif (ejercicio == 'tarjeta'):
                mensaje = validar_tarjeta(parametros)
            elif (ejercicio == 'palabra'):
                mensaje = validar_palabra(parametros)
        
    # El ejercicio de dibujar la figura SVG es el único que no necesita parámetros
    # y por tanto, no necesitaremos introducir nada en el formulario
    elif (ejercicio == 'svg'):
        mensaje = svg()

    if (ejercicio == 'burbuja' or ejercicio == 'seleccion' or
        ejercicio == 'criba' or ejercicio == 'fibonacci' or
        ejercicio == 'corchetes' or ejercicio == 'correo' or
        ejercicio == 'tarjeta' or ejercicio == 'palabra' or ejercicio == 'palabra'):

        update_paginas('/interfaz_ejercicios/' + nombre + '/' + ejercicio, nombre)
    else:
        return redirect(url_for(ejercicio))

    return render_template('interfaz_ejercicios.html', 
        nombre = nombre, ejercicio = ejercicio, mensaje = mensaje, 
            paginas = paginas, usuario = usuario)


@app.errorhandler(404)
def page_not_found(error):
    return "<h1 style=\"color:red; text-align:center\";>Página no encontrada</h1>", 404

############################
# Práctica 4:
############################

@app.route('/pokedex')
def pokedex():
    update_paginas('pokedex', 'Pokédex')
    usuario = get_user_session()
	# Encontramos los documentos de la coleccion "samples_pokemon"
    coleccion_pokemon = db.samples_pokemon.find() # devuelve un cursor(*), no una lista ni un iterador

    todos_pokemon = []
    for pokemon in coleccion_pokemon:
	    app.logger.debug(pokemon) # salida consola
	    todos_pokemon.append(pokemon)

	# a los templates de Jinja hay que pasarle una lista, no el cursor
    return render_template('pokemon.html', todos_pokemon = todos_pokemon,
        paginas = paginas, usuario = usuario)
