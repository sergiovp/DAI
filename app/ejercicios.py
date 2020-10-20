# Para el ejercicio de expresiones regulares:
import re

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
    numero = int(numero)
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
    numero = int(numero)
    # First Fibonacci number is 0
    if (numero == 1):
        return 0

    # Second Fibonacci number is 1
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
    #^(?:[0-9]{4}-){3}[0-9]{4}|[0-9]{16}
    #expresion = '^\d{4}-'
    #expresion = '/[^\d]\d{4}[^\d]/'
    #expresion = '^\d{4}\s{1}|-{1}'
    #expresion = '(?:\d{4}-|\s?){3}\d{4}'
    expresion = '^\d{4}(?:-|\s)\d{4}(?:-|\s)\d{4}(?:-|\s)\d{4}$'

    if (re.search(expresion, tarjeta)):
        return True
    return False