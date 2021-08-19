# AED-TP3
Este es el tercer trabajo práctico para la materia "Algoritmos y Estructuras de Datos" de la UTN-FRC

## Consigna:
Una tienda de libros electrónicos nos solicita ayuda para desarrollar un sistema de gestión de sus productos. De cada libro se conoce:

    Código de identificación o ISBN (cadena de caracteres).
    Título.
    Género (0: Autoayuda, 1:Arte, 2: Ficción, 3: Computación, 4: Economía, 5: Escolar, 6: Sociedad, 7: Gastronomía, 8: Infantil , 9: Otros).
    Idioma (1: español, 2: inglés, 3: francés, 4:italiano, 5:otros).
    Precio.

Se solicita un programa controlado por menú de opciones que permita lo siguiente:

### 1.) Generación y Carga: 
Generar un arreglo unidimensional con los n libros que ofrece la librería (n es un valor que se ingresa por teclado). Para el presente práctico se solicita que el usuario pueda optar por una carga manual (validando los datos de entrada) o por una carga automática de los datos de cada libro.
Se debe tener en cuenta que el International Standard Book Number (ISBN) es un identificador único para libros creado para uso comercial. Se creó en 1966 en el Reino Unido y alcanzó el rango de estándar internacional en 1970. Todas las ediciones y variaciones de un libro reciben un ISBN de 10 dígitos dividido en los cuatro grupos que se indican a continuación (sin longitud fija por cada grupo) separados por guiones ("-"):

        Código de país o lengua de origen.
        Código del editor (asignado por la agencia nacional del ISBN).
        Número del artículo (elegido por el editor).
        Dígito de control.

Se sabe que sus dígitos x1, x2, x3, ..., x10 satisfacen la relación:

En definitiva, el resto de dividir esa suma por 11, debe dar cero. Por ejemplo, para el siguiente ISBN: 84-8181-227-7 se comprueba que:  10*8+9*4+8*8+7*1+6*8+5*1+4*2+3*2+2*7+7 = 275 y al dividir 275 por 11 vemos que el resto es 0. Lo que nos indica que es un ISBN válido (275 % 11 = 0).

    El siguiente ISBN 5555687-525 no es válido porque no tiene los 4 grupos.
    El ISBN 456--55-25438 tiene los 10 dígitos, y la cantidad de guiones correcta pero no tiene los 4 grupos dado que hay dos guiones seguidos.
    Para el ISBN 451-567-43-89 se comprueba que: 10*4+9*5+8*1+7*5+6*6+5*7+4*4+3*3+2*8+9 = 249 y al dividir por 11 el resto no es cero, lo que nos indica que no es un ISBN válido.

### 2.) Mostrar: 
Mostrar el vector generado en el punto anterior de tal manera que se muestre el género y el idioma del libro en lugar de los números que los representan y se listen ordenados por título en forma ascendente. Cada libro debe mostrarse a razón de una línea por registro.

### 3.) Conteo y género más popular: 
Determinar la cantidad de libros ofrecidos por género. Mostrar dichas cantidades y el género al que corresponde mostrando su nombre y no su código. Determinar el género con mayor cantidad de libros ofrecidos, indicando su nombre. Si hubiera más de un género con la misma cantidad, informar uno solo.

### 4.) Búsqueda del mayor: 
Determinar y mostrar el libro de mayor precio para un idioma i, siendo i un valor que se ingresa por teclado. Si existiera más de un libro con el mismo mayor precio mostrar sólo uno.

### 5.) Búsqueda por ISBN: 
Buscar si en el vector existe un libro con el ISBN x, siendo x un valor que se ingrese por teclado. Si existe mostrar sus datos y aumentar su precio un 10%. Si no existe, mostrar un mensaje por pantalla.

### 6.) Consulta de un género: 
Mostrar los datos de los libros del género con mayor cantidad de libros identificado en el punto 3. Dicho listado debe mostrarse ordenado por precio de mayor a menor.

### 7.) Consulta de precio por grupo: 
Esta funcionalidad permite a los alumnos secundarios cargar el listado de los ISBN correspondientes a los libros que el colegio les exige para el año escolar. El sistema debe buscar cuáles de estos libros se encuentran en su catálogo e indicar:

        Los libros que no se encontraron en el catálogo.
        Los libros que sí se encontraron en el catálogo con su precio.
        El precio total que el estudiante debería pagar para comprar aquellos libros que la librería vende.
