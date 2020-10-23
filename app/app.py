import ejercicios

from flask import Flask, render_template
app = Flask(__name__)
          
@app.route('/')
def hola():
    return '<h1>Hola gente</h1>'
    #return render_template('index.html')

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

@app.route('/criba/<int:numero>')
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