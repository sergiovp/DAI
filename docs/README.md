En este directorio podrás encontrar documentación relativa al desarrollo de las prácticas, así como los enunciados o tareas propuestos para éstas.

## Práctica 1. Python y entorno de trabajo con docker

Esta práctica tiene como objetivo preparar el entorno de trabajo que usaremos (*instalación de docker y docker-compose*) así como familiarizarse con el lenguaje de programación que utilizaremos en la asignatura, (*python*).

Tras la instalación de [docker](https://docs.docker.com/get-docker/) y [docker-compose](https://docs.docker.com/compose/install/), se nos propone una serie de programas a desarrollar en python:

1. Programe un mini-juego de "adivinar" un número (entre 1 y 100) que el ordenador establezca al azar. El usuario puede ir introduciendo números y el ordenador le responderá con mensajes del estilo "El número buscado el mayor / menor". El programa debe finalizar cuando el usuario adivine el número (con su correspondiente mensaje de felicitación) o bien cuando el usuario haya realizado 10 intentos incorrectos de adivinación.

2. Programe un par de funciones de ordenación de matrices (UNIDIMENSIONALES) de números distintas (burbuja, selección, inserción, mezcla, montículos...) (Wikipedia: Algoritmo de ordenamiento). Realice un programa que genere aleatoriamente matrices de números aleatorios y use dicho métodos para comparar el tiempo que tardan en ejecutarse.

3. La Criba de Eratóstenes es un sencillo algoritmo que permite encontrar todos los números primos menores de un número natural dado. Prográmelo.

4. Cree un programa que lea de un fichero de texto un número entero n y escriba en otro fichero de texto el n-ésimo número de la sucesión de Fibonacci.

5. Cree un programa que:
    + Genere aleatoriamente una cadena de [ y ].
    + Compruebe mediante una función si dicha secuencia está balanceada, es decir, que se componga de parejas de corchetes de apertura y cierre correctamente anidados. Por ejemplo:
        + `[]` -> Correcto
        + `[[][[]]]` -> Correcto
        + `[][]` -> Correcto
        + `][` -> Incorrecto
        + `[[][[` -> Incorrecto
        + `[]][[]` -> Incorrecto

6. Utilizando expresiones regulares realice funciones para:
    + Identificar cualquier palabra seguida de un espacio y una única letra mayúscula (por ejemplo: Apellido N).
    + Identificar correos electrónicos válidos (empieza por una expresión genérica y ve refinándola todo lo posible).
    + Identificar números de tarjeta de crédito cuyos dígitos estén separados por - o espacios en blanco cada paquete de cuatro dígitos: 1234-5678-9012-3456 ó 1234 5678 9012 3456.

Para más detalle sobre la práctica, consultad [este enlace](https://swad.ugr.es/swad/tmp/am/knPrklOpnqvSFhoykCDmiu8onz84DmtYdv49AC6G4/DAI%20Practica%201%20-%20Python%20y%20entorno%20de%20trabajo.html).

---

## Práctica 2. Microframework Flask

En esta práctica se nos propone crear el entorno necesario para ejecutar un *hola mundo* haciendo uso del microframework [flask](https://palletsprojects.com/p/flask/), con el que podremos desarrollar aplicaciones web en poco tiempo.

**Creación del entorno:**

+ Crear imagen de docker ([Dockerfile](https://github.com/sergiovp/DAI/blob/master/Dockerfile)) que contendrá las órdenes para instalar bibliotecas, variables de entorno, etc.

+ Fichero [requirements.txt](https://github.com/sergiovp/DAI/blob/master/requirements.txt) en el que especificaremos las bibliotecas y versiones para `pip`.

+ Fichero [docker-compose.yml](https://github.com/sergiovp/DAI/blob/master/docker-compose.yml) para usar nuestra imagen de docker.

+ Fichero [app.py](https://github.com/sergiovp/DAI/blob/master/app/app.py) con el `hola mundo`.

Los ejercicios propuestos para esta práctica son los siguientes:

1. Hacer un interface web para los ejercicios 2-6 de la práctica anterior. La entrada se hará por URL p.e: `http://localhost:5000/ordena/5,2,7,3`.

2. Crear una página servida desde un directorio static, con las direcciones del ejercicio anterior.

3. Crear una página para el caso en que una URL no esté definida (error HTTP 404, not found).

Para más detalle sobre la práctica, consultad [este enlace](https://swad.ugr.es/swad/tmp/Gh/CxSslYczx9vm9CRv20lg1QX-osPNX4qM55FaguO4Q/DAI%20Practica%202%20-%20Microframework%20Flask.html).

## Práctica 3. Plantillas, Manejo de Sesiones y Frameworks CSS

Se propone avanzar en el uso de Flask. Eneste caso incluiremos el uso de un motor de plantillas, *Jinja*. Dicho motor se encuentra incorporado en Flask. Haremos uso de un flamework de CSS para hacer que el HTML sea adaptable y utilizaremos sesiones para gestionar la identificación de usuarios en la aplicación.

En resumen, las herramientas que utilizaremos son las siguientes:

+ Framework aplicación web: **Flask**
+ Motor de plantillas: **Jinja** (incorporado en Flask)
+ Framework CSS: **Bootstrap**
+ Almacenamiento local: **pickleshare**

Tras la realización de la práctica, la web deberá incluir una barra de navegación dando la opción de logearse o registrarse a los usuarios, así como enlaces a otras páginas.
Un aside o menú lateral junto a un espacio para mostrar contenidos y un footer al final de la web.
