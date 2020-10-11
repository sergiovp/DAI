# DAI
Repositorio dedicado a la asignatura Desarrollo de Aplicaciones para Internet cursada en la UGR (2020/21).

---

## Práctica 1

Esta práctica tiene como objetivo preparar el entorno de trabajo que usaremos (instalación de docker y docker-compose) así como familiarizarse con el lenguaje de programación que utilizaremos en la asignatura, (python).

Tras la instalación de [docker](https://docs.docker.com/get-docker/) y [docker-compose](https://docs.docker.com/compose/install/), se nos propone una serie de programas a desarrollar en python:

1. Programe un mini-juego de "adivinar" un número (entre 1 y 100) que el ordenador establezca al azar. El usuario puede ir introduciendo números y el ordenador le responderá con mensajes del estilo "El número buscado el mayor / menor". El programa debe finalizar cuando el usuario adivine el número (con su correspondiente mensaje de felicitación) o bien cuando el usuario haya realizado 10 intentos incorrectos de adivinación.

2. Programe un par de funciones de ordenación de matrices (UNIDIMENSIONALES) de números distintas (burbuja, selección, inserción, mezcla, montículos...) (Wikipedia: Algoritmo de ordenamiento). Realice un programa que genere aleatoriamente matrices de números aleatorios y use dicho métodos para comparar el tiempo que tardan en ejecutarse.

3. La Criba de Eratóstenes es un sencillo algoritmo que permite encontrar todos los números primos menores de un número natural dado. Prográmelo.

4. Cree un programa que lea de un fichero de texto un número entero n y escriba en otro fichero de texto el n-ésimo número de la sucesión de Fibonacci.

5. Cree un programa que:
    + Genere aleatoriamente una cadena de [ y ].
    + Compruebe mediante una función si dicha secuencia está balanceada, es decir, que se componga de parejas de corchetes de apertura y cierre correctamente anidados. Por ejemplo:
        + [] -> Correcto
        + [[][[]]] -> Correcto
        + [][] -> Correcto
        + ][ -> Incorrecto
        + [[][[ -> Incorrecto
        + []][[] -> Incorrecto

6. Utilizando expresiones regulares realice funciones para:
    + Identificar cualquier palabra seguida de un espacio y una única letra mayúscula (por ejemplo: Apellido N).
    + Identificar correos electrónicos válidos (empieza por una expresión genérica y ve refinándola todo lo posible).
    + Identificar números de tarjeta de crédito cuyos dígitos estén separados por - o espacios en blanco cada paquete de cuatro dígitos: 1234-5678-9012-3456 ó 1234 5678 9012 3456.
