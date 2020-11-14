# Para el ejercicio de expresiones regulares:
import re

# Para el random
import random

# Ordenar vector usando burbuja
def burbuja_sort(vector):
    n = len(vector)

    for i in range(n):
        for j in range(i, n - 1):
            if (vector[i] > vector[j + 1]):
                vector[i], vector[j + 1] = vector[j + 1], vector[i]

    return vector

# Ordenar vector usando selección
def seleccion_sort(vector):
    n = len(vector)

    for i in range(n):
        for j in range(i + 1, n):
            if (vector[j] < vector[i]):
                vector[i], vector[j] = vector[j], vector[i]

    return vector

# Reemplazar las ',' de un string por espacios en blanco
def clean_list(string):
    return string.replace(',', ' ')

# Saca los números primos menores que un número dado
def criba_eratostenes(numero):
    if (numero == 0 or numero == 1):
        return []
    primos = []
    es_primo = [1 for i in range(numero)]
    es_primo[0] = es_primo[1] = 0

    for i in range(numero):
        if es_primo[i]:
            primos.append(i)
            h = 2
            while i * h < numero:
                es_primo[i * h] = 0
                h += 1

    return primos

# Saca el n-ésimo número de la sucesión de Fibonacci
def sucesion_fibonacci(numero):
    # El primer número es un 0
    if (numero == 1):
        return 0

    # El segundo número es un 1
    elif (numero == 2):
        return 1

    else:
        return sucesion_fibonacci(numero - 1) + sucesion_fibonacci(numero - 2)

# Devuelve si un string de corchetes es "balanceado"
def is_balanceado(corchetes):
    corchete_abierto = "["
    corchete_cerrado = "]"
    pila = []

    for i in corchetes: 
        if i in corchete_abierto: 
            pila.append(i) 
        
        elif i in corchete_cerrado: 
            pos = corchete_cerrado.index(i) 
            if ((len(pila) > 0) and (corchete_abierto[pos] == pila[len(pila) -1])): 
                pila.pop()
            else:
                return False

    if len(pila) == 0:
        return True
    else:
        return False
    
# Nos devuelve si el nombre de un correo es válido
def check_correo(correo):
    expresion = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if (re.search(expresion, correo)):
        return True
    return False

def check_tarjeta(tarjeta):
    expresion = '^\d{4}(?:-|\s)\d{4}(?:-|\s)\d{4}(?:-|\s)\d{4}$'

    if (re.search(expresion, tarjeta)):
        return True
    return False

def check_palabra(palabra):
    expresion = '^[A-Za-z]+ ([A-Z]){1}$'

    if (re.search(expresion, palabra)):
        return True
    return False

def crear_figura():
    colores = ['azure', 'coral', 'darkslategray', 'dodgerblue', 'indigo', 'lightgreen',
    'lightseagreen', 'lightsteelblue', 'midnightblue', 'plum', 'violet', 'palegreen',
    'mediumseagreen']

    # Propiedades círculo
    color_c = random.choice(colores)
    borde_c = random.choice(colores)
    cx = random.randrange(50, 1000)
    cy = random.randrange(50, 380)
    r = random.randrange(30, 200)

    # Propiedades rectángulo
    color_r = random.choice(colores)
    borde_r = random.choice(colores)
    rx = random.randrange(0, 1000)
    ry = random.randrange(50, 380)
    width = random.randrange(50, 300)
    height = random.randrange(50, 300)

    svg_start = '<svg width="1200" height="390">'
    svg_circle = '<circle cx="'+str(cx)+'" cy="'+str(cy)+'" r="'+str(r)+'" stroke="'+borde_r+'" stroke-width="1" fill="'+color_r+'" />'
    svg_end = '</svg>'
    
    svg_rectangle = '<rect x="'+str(rx)+'" y="'+str(ry)+'"  width="'+str(width)+'" height="'+str(height)+'"fill="'+color_c+'"stroke="'+borde_c+'"/>'

    return svg_start + svg_circle + svg_rectangle + svg_end
