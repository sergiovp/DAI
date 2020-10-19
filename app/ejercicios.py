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
