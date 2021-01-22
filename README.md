# DAI
Repositorio dedicado a la asignatura Desarrollo de Aplicaciones para Internet cursada en la UGR (2020/21).

---

## Documentación

En el directorio [docs](https://github.com/sergiovp/DAI/tree/master/docs) encontrarás documentación relativa al desarrollo de las prácticas de la asignatura, así como los objetivos a cumplir en cada una de éstas.

## Despliegue aplicación Django

> Nota: Como requisito es necesario tener instalado **git**, **docker** y **docker-compose**.

Clonamos el repositorio:
~~~
git clone https://github.com/sergiovp/DAI
~~~

Nos movemos hacia el directorio de la aplicación:
~~~
cd DAI/DjangoApp/
~~~

Ejecutamos la aplicación:
~~~
make
~~~

> La orden 'make' levantará el contenedor haciendo `docker-compose up`

Desde el navegador accedemos a la app:
~~~
localhost
~~~

> Notas:
>> 1. Si altera ficheros Dockerfile o docker-compose.yml, puede reconstruirlos con `make build`
>> 2. Si altera los modelos de la app, ejecute `make migrations` y `make migrate`


## Práctica 1 y 2. Python y entorno de trabajo con docker y Microframework Flask.

> NOTA: para más información sobre la práctica, se puede consultar el siguiente [fichero](https://github.com/sergiovp/DAI/blob/master/docs/README.md)

Para ver el resultado de ambas prácticas podemos acceder a la siguiente URL:
~~~
localhost:5000/static/index.html
~~~

En dicha página podemos ver una sencilla interfaz con la cual podremos acceder a la ejecución de los distintos ejercicios pinchando en cada enlace.

## Práctica 3. Plantillas, Manejo de Sesiones y Frameworks CSS

> NOTA: para más información sobre la práctica, se puede consultar el siguiente [fichero](https://github.com/sergiovp/DAI/blob/master/docs/README.md)

Para ver el resultado, accederemos con la siguiente URL:
~~~
localhost:5000
~~~

En esta práctica podremos registrarnos en la web, visualizar nuestros datos y modificarlos una vez estemos logeados y también tendremos la posibilidad de ejecutar los ejercicios de las prácticas anteriores con una interfaz implementada para ello.

A lo anterior comentado se puede acceder con los enlaces desde el menú de navegación.

También se ha implementado un elemento en el menú que muestre las tres últimas páginas visitadas de nuestra web.

## Práctica 4. Bases de Datos NoSQL, CRUD

> NOTA: para más información sobre la práctica, se puede consultar el siguiente [fichero](https://github.com/sergiovp/DAI/blob/master/docs/README.md)

En este caso, trabajaremos con bases de datos no relaciones, en concreto con MongoDB.

Para ello, nos hemos descargado una BD de prueba, en este caso, de Pokémon.

Si accedemos a la aplicación, veremos que hay un elemento en el menú llamado "Pokémon". En él podemos ver todos los Pokémon de la Pokédex de Kanto. Podremos modificar el nombre de cada uno de los Pokémon, así como eliminar o incluso filtrar por nombre.

## Práctica 5. API REST

> NOTA: para más información sobre la práctica, se puede consultar el siguiente [fichero](https://github.com/sergiovp/DAI/blob/master/docs/README.md)

Esta página ha consistido en la implementación de una pequeña API. Nos encargaremos de responder distintas peticiones que nos lleguen.

Las peticiones las podemos realizar mediante el comando *CURL*, por ejemplo. Cabe destacar que toda respuesta será en formato *JSON* y que las funciones gestionan los errores posibles generados durante la petición (no parámetros, parámetros incorrectos, no encuentra el ID en la BD, etc).

Dichas peticiones son las siguientes:

+ **curl -X GET localhost:5000/api/pokemon** Nos responderá con todos los Pokémon de nuestra DB

+ **curl -X POST localhost:5000/api/pokemon -d "numero=NUMERO&nombre=NOMBRE&img=URL_IMG"** Añadirá a la BD el Pokémon con NÚMERO, NOMBRE y URL_IMAGEN especificados

+ **curl -X DELETE localhost:5000/api/delete/ID** Eliminará el Pokémon cuyo ID coincida con el de la URL

+ **curl -X GET localhost:5000/api/filtro_pokemon?name=NAME** Nos mostrará los Pokémon cuyo nombre se asemeje al NAME introducido

+ **curl -X PUT localhost:5000/api/mod_pokemon/ID -d "numero=NUMERO&nombre=NOMBRE&img=URL_IMG"** Modificará los datos del Pokémon cuyo ID coincida con el introducido. Dichos datos serán sustituidos por NUMERO, NOMBRE y URL_IMAGEN
