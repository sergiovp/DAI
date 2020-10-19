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