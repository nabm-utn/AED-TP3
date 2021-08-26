"""
Este es el programa principal. A continuación voy a armar una estructura base a partir de comentarios.
"""
from libro import *
# ============================================= #
# Parte 0 Funciones Auxiliares
# ============================================= #


def validar_positivo(n, minimo):
    return minimo <= n


def validar_genero(genero):
    return 0 <= genero <= 9


def validar_idioma(idioma):
    return 1 <= idioma < 5


def maximo(vector):
    """
    Devuelve el índice del valor máximo de un vector. Si hay más de un valor máximo retorna solo el primero
    Es equivalente (aunque con peor performance) al builtin max()
    :param vector: un iterable con valores numéricos
    :return: el indice del valor mayor del vector provisto
    """
    maximo = -9999
    maximo_index = None
    index = 0
    for elemento in vector:
        if elemento > max:
            maximo = elemento
            maximo_index = index
        index += 1
    return maximo_index


def genero_to_str(genero):
    if not 0 <= genero <= 9:
        return "genero desconocido"
    generos = ("Autoayuda", "Arte", "Ficción", "Computación", "Economía",
               "Escolar", "Sociedad", "Gastronomía", "Infantil", "Otros")
    return generos[genero]


# ............................................. #
# Parte 0.1 Menú de Opciones General
# ............................................. #


def menu_de_opciones():
    opcion = None
    menu = """
Menú de opciones
----------------
1.) Generar y cargar el catálogo de libros a la venta
2.) Ver el catálogo en orden alfabético
3.) Ver la cantidad de libros por género y conocer el género con mayor cantidad de libros
4.) Verificar el libro más caro para un idioma
5.) Aumentar 10% el precio de un libro (se ingresa el ISBN)
6.) Consultar listado de libros del género más numeroso, ordenado de mayor a menor precio
7.) Consultar existencia de libros escolares solicitados para el ciclo lectivo y obtener precio por grupo
8.) Finalizar programa"""
    while opcion != '8':
        print(menu)
        opcion = input('Ingrese opción: ')
        if opcion == '1':
            # opcion1()
            pass
        elif opcion == '2':
            pass
            # opcion2()
        elif opcion == '3':
            pass
            # opcion3()
        elif opcion == '4':
            pass
            # opcion4()
        elif opcion == '5':
            pass
            # opcion5()
        elif opcion == '6':
            pass
            # opcion6()
        elif opcion == '7':
            pass
            # opcion7()
        elif opcion == '8':
            confirmacion = input('Seleccionó finalizar programa. ¿Está seguro que desea salir? s/n: ')
            if confirmacion == 's' or confirmacion == 'S':
                print('Gracias por utilizar este programa. Hasta pronto.')
            else:
                opcion = None
        else:
            print('La opción ingresada no es válida')


# ............................................. #
# Parte 0.2 Validación ISBN
# ............................................. #
# => HECHO en libro.py

# ............................................. #
# Parte 0.3 Ordenar arreglo
# ............................................. #

# ============================================= #
# Parte 1 Generación del vector de registros.
# ============================================= #

catalogo_principal = []

# ............................................. #
# Parte 1.1 Generación Automática
# ............................................. #
cargado_automatico = True

if cargado_automatico:
    catalogo_principal += auto_fill(30)

# ............................................. #
# Parte 1.2 Generación Manual
# ............................................. #


def generar_libro_manual():
    isbn = input('Código de Identificación (ISBN): ')
    while not validar_isbn(isbn):
        print('Error. ISBN no válido, ingrese otro.')
        isbn = input('Código de Identificación (ISBN): ')
    titulo = input('Título: ')
    genero = int(input('Género (0-9): '))
    while not validar_genero(genero):
        print('Error. Los códigos para identificar el género van del 0 al 9, ingrese otro.')
        genero = int(input('Género (0-9): '))
    idioma = int(input('Idioma (1-5): '))
    while not validar_idioma(idioma):
        print('Error. Los códigos para identificar idioma van del 1 al 5, ingrese otro.')
        idioma = int(input('Idioma (1-5): '))
    precio = round(float(input('Precio: $')), 2)
    while not validar_positivo(precio, 0):
        print('Error, para cargar el precio no se admiten valores negativos, ingrese otro valor.')
        precio = round(float(input('Precio: $')), 2)
    return Libro(isbn, titulo, genero, idioma, precio)


def generar_catalogo_manual(n):
    catalogo = []
    for i in range(n):
        catalogo.append(generar_libro_manual())
    return catalogo


# ============================================= #
# Parte 2 Manipulación del vector de registros.
# ============================================= #

# ............................................. #
# Parte 2.1 Display General
# ............................................. #
# -> Ordenar todo el arreglo alfabéticamente por titulo
# -> Mostrar todos los libros con genero e idioma decodificados

# ............................................. #
# Parte 2.2 Popularidad de Genero
# ............................................. #
# -> Vector de Conteo


def contar_x_genero(catalogo):
    contador = 10 * [0]
    for libro in catalogo:
        contador[libro.genero] += 1
    return contador


def display_x_genero(contador):
    for i in range(len(contador)):
            print("El genero {} contiene: {:02d} libros".format(genero_to_str(i)), contador[i])


def conteo_y_genero_popular(catalogo):
    contador = contar_x_genero(catalogo)
    display_x_genero(contador)
    genero_popular = maximo(contador)
    cantidad_popular = contador[genero_popular]
    print("El género más popular es {} con un total de {} libros".format(genero_popular, cantidad_popular))


# ............................................. #
# Parte 2.3 Libro mas caro segun idioma
# ............................................. #
# -> Vector de registros de un dado idioma
# -> encontrar el mayor y mostrarlo


def sub_catalogo_idioma(catalogo, idioma):
    """
    :param catalogo: un vector de registros del tipo libro
    :param idioma: un entero entre 1 y 5 que codifica un idioma
    :return: un vector con el subconjunto de libros del idioma especificado
    """
    return [libro for libro in catalogo if libro.idioma == idioma]


def libro_mas_caro(catalogo):
    """
    :param catalogo: un vector de registros del tipo libro
    :return: el libro con el mayor precio del vector
    """
    precio_max = -9999
    libro_max = None
    for libro in catalogo:
        if libro.precio > precio_max:
            libro_max = libro
            precio_max = libro_max.precio
    return libro_max


def libro_mas_caro_idioma(catalogo, idioma):
    """
    Imprime un mensaje indicando el libro más caro del idioma especificado

    :param catalogo: un vector de registros del tipo libro
    :param idioma: un entero entre 1 y 5 que codifica un idioma
    :return: None
    """
    idiomas = ("español", "ingles", "frances", "italiano", "otros")
    idioma_str = idiomas[idioma-1]
    print("El libro más caro escrito en el idioma {}:".format(idioma_str))
    print(libro_mas_caro(sub_catalogo_idioma(catalogo, idioma)))


if __name__ == "__main__":
    for idioma in range(1, 6):
        libro_mas_caro_idioma(catalogo_principal, idioma)


# ............................................. #
# Parte 2.4 Busqueda por ISBN
# ............................................. #
# -> Validar ISBN
# -> Buscar si hay coincidencia
# -> Mostrar datos
# -> Aumentar precio (10%)


def busqueda_por_isbn(catalogo, isbn):
    for libro in catalogo:
        if libro.isbn == isbn:
            return libro
    return False


def aumentar_10(libro):
    confirma = input("Presione s para subir precio 10%")
    if confirma == "s" or confirma == "S":
        libro.precio *= 1.1
        print("El nuevo precio es: ${}".format(libro.precio))
    else:
        print("Se mantiene el precio original: ${}".format(libro.precio))


def buscar_y_subir_precio(catalogo, isbn):
    if not validar_isbn():
        print("El ISBN solicitado no es válido")
        return
    libro = busqueda_por_isbn(catalogo, isbn)
    if libro:
        print("Libro encontrado:")
        print(libro)
        aumentar_10(libro)
    else:
        print("No se encontró el libro en cuestión")


# ............................................. #
# Parte 2.5 Display Libros Genero Popular
# ............................................. #
# -> Usar codigo de 2.2
# -> Generar un vectorcito de libros del genero
# -> Ordenarlo
# -> Mostrarlo

def sub_catalogo_genero(catalogo, genero):
    return [libro for libro in catalogo if libro.genero == genero]


def ordenar_x_precio(catalogo):
    pass


def mostrar_genero_popular(catalogo):
    genero_popular = maximo(contar_x_genero(catalogo))
    catalogo = sub_catalogo_genero(catalogo, genero_popular)
    ordenar_x_precio(catalogo)
    print("\nListado de libros del genero más popular ({}):".format(genero_to_str(genero_popular)))
    for libro in catalogo:
        print(libro)


# ............................................. #
# Parte 2.6 Consulta Combo
# ............................................. #
# -> Usar codigo de 2.4
# -> Acumulador de precio
# -> Mostrar resultados

def solicitar_codigos():
    print("A continuación, deberá introducir los códigos de los libros que sean de su interes.")
    exit = False
    codigos = []
    while not exit:
        print("Hasta ahora se han cargado {} codigos.".format(len(codigos)))
        isbn = input("Por favor ingres un código ISBN válido. Ingrese 0 para salir")
        if isbn == "0":
            exit = True
        elif validar_isbn(isbn):
            codigos.append(isbn)
        else:
            print("Codigo inválido")
    return codigos


def consulta_combo(catalogo):
    codigos = solicitar_codigos()
    # Busca libros en el catalogo segun isbn
    encontrados = [codigo for codigo in codigos if codigo in [libro.isbn for libro in catalogo]]
    no_encontrados = [codigo for codigo in codigos if codigo not in encontrados]

    # Avisa que libros no se encontraron
    if len(no_encontrados) > 0:
        print("No se encontraron libros que correspondan a los siguientes {} códigos:".format(len(no_encontrados)))
        for codigo in no_encontrados:
            print(codigo)

    #Trabaja con los libros que se encontraron
    if len(encontrados) > 0:
        print("Se encontraron los siguientes {} libros:".format(len(encontrados)))
        encontrados = [libro for libro in catalogo if libro.isbn in encontrados]
        precio_total = 0
        for libro in encontrados:
            print(libro)
            precio_total += libro.precio
        print("\n"+"-"*60)
        print("El precio por todos los libros es de: ${}".format(precio_total))
    else:
        print("No se encontró ningún libro de los solicitados")

