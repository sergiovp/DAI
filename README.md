# DAI
Repositorio dedicado a la asignatura Desarrollo de Aplicaciones para Internet cursada en la UGR (2020/21).

---

## Documentación

En el directorio [docs](https://github.com/sergiovp/DAI/tree/master/docs) encontrarás documentación relativa al desarrollo de las prácticas de la asignatura, así como los objetivos a cumplir en cada una de éstas.

## Despliegue

> Nota: Como requisito es necesario tener instalado **git**, **docker** y **docker-compose**.

Clonamos el repositorio:
~~~
git clone https://github.com/sergiovp/DAI
~~~

Ejecutamos la aplicación:
~~~
make
~~~

> Nota: la orden 'make' levantará el contenedor haciendo `docker-compose up`.

Desde el navegador ponemos la URL:
~~~
localhost:5000
~~~

## Práctica 1 y 2.

> NOTA: para más información sobre la práctica, se puede consultar el siguiente [fichero](https://github.com/sergiovp/DAI/blob/master/docs/README.md)

Para ver el resultado de ambas prácticas podemos acceder a la siguiente URL:
~~~
localhost:5000/static/index.html
~~~

En dicha página podemos ver una sencilla interfaz con la cual podremos acceder a la ejecución de los distintos ejercicios pinchando en cada enlace.

## Práctica 3.

> NOTA: para más información sobre la práctica, se puede consultar el siguiente [fichero](https://github.com/sergiovp/DAI/blob/master/docs/README.md)

Para ver el resultado, accederemos con la siguiente URL:
~~~
localhost:5000
~~~

En esta práctica podremos registrarnos en la web, visualizar nuestros datos y modificarlos una vez estemos logeados y también tendremos la posibilidad de ejecutar los ejercicios de las prácticas anteriores con una interfaz implementada para ello.

A lo anterior comentado se puede acceder con los enlaces desde el menú de navegación.
