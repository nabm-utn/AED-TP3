from libro import Libro
from helper import input_positivo, validar_genero, validar_idioma, indice_maximo, genero_to_str, idioma_to_str
from isbn import validar_isbn, isbn_error_msj
from auto import auto_fill


# ============================================= #
# Consigna 1 Generación del vector de registros.
# ============================================= #
def actualizar_catalogo(catalogo):
    menu = """Libros en el catálogo: {}
Por favor seleccione el tipo de carga a realizar
1.) Manual
2.) Automática
3.) Cancelar"""
    opcion = None
    while opcion != "3":
        print(menu.format(len(catalogo)))
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            catalogo += generar_catalogo_manual()
        elif opcion == "2":
            catalogo += generar_catalogo_automatico()


def generar_catalogo_automatico():
    n = input_positivo("Ingrese la cantidad de libros a generar (0 para cancelar): ")
    return auto_fill(n)


def generar_catalogo_manual():
    catalogo = []
    n = input_positivo("Ingrese la cantidad de libros a generar (0 para cancelar): ")
    for i in range(n):
        print("\nLibro {} de {}".format(i+1, n))
        catalogo.append(generar_libro_manual())
    return catalogo


def solicitar_isbn():
    isbn = input('Código de Identificación (ISBN): ')
    while not validar_isbn(isbn):
        print(isbn_error_msj(isbn))
        isbn = input('Código de Identificación (ISBN): ')
    return isbn


def solicitar_genero():
    genero = int(input('Género (0-9): '))
    while not validar_genero(genero):
        print('Error. Los códigos para identificar el género van del 0 al 9, ingrese otro.')
        genero = int(input('Género (0-9): '))
    return genero


def solicitar_idioma():
    idioma = int(input('Seleccione un idioma (1-5): '))
    while not validar_idioma(idioma):
        print('Error. Los códigos para identificar idioma van del 1 al 5, ingrese otro.')
        idioma = int(input('Idioma (1-5): '))
    return idioma


def solicitar_precio():
    precio = input_positivo("Precio: $", is_float=True)
    return round(precio, 2)


def generar_libro_manual():
    isbn = solicitar_isbn()
    titulo = input('Título: ')
    genero = solicitar_genero()
    idioma = solicitar_idioma()
    precio = solicitar_precio()
    return Libro(isbn, titulo, genero, idioma, precio)


# ............................................. #
# Consigna 2 Display General
# ............................................. #
def mostrar_libros_ordenados(catalogo):
    ordenar_por_titulo(catalogo)
    print("Estos son los libros disponibles")
    for libro in catalogo:
        print(libro)


def ordenar_por_titulo(catalogo):
    n = len(catalogo)
    h = 1
    while h <= n // 9:
        h = 3 * h + 1

    while h > 0:
        for j in range(h, n):
            y = catalogo[j]
            k = j - h
            while k >= 0 and y.titulo < catalogo[k].titulo:
                catalogo[k + h] = catalogo[k]
                k -= h
            catalogo[k + h] = y
        h //= 3


# ............................................. #
# Consigna 3 Popularidad de Genero
# ............................................. #
def conteo_y_genero_popular(catalogo):
    contador = contar_x_genero(catalogo)
    display_x_genero(contador)
    genero_popular = indice_maximo(contador)
    cantidad_popular = contador[genero_popular]
    genero_popular = genero_to_str(genero_popular)
    print("El género más popular es {} con un total de {} libros".format(genero_popular, cantidad_popular))


def contar_x_genero(catalogo):
    contador = 10 * [0]
    for libro in catalogo:
        contador[libro.genero] += 1
    return contador


def display_x_genero(contador):
    for i in range(len(contador)):
        print("El genero {} contiene: {:02d} libros".format(genero_to_str(i), contador[i]))


# ............................................. #
# Consigna 4 Libro mas caro segun idioma
# ............................................. #
def libro_mas_caro_por_idioma(catalogo):
    """
    Imprime un mensaje indicando el libro más caro del idioma especificado

    :param catalogo: un vector de registros del tipo libro
    :return: None
    """
    idioma = solicitar_idioma()
    libro = libro_mas_caro(sub_catalogo_idioma(catalogo, idioma))
    if libro:
        print("\nEl libro más caro escrito en el idioma {}:".format(idioma_to_str(idioma)))
        print(libro)
    else:
        print("No se encontraron libros para el idioma {}".format(idioma_to_str(idioma)))


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


def sub_catalogo_idioma(catalogo, idioma):
    return [libro for libro in catalogo if libro.idioma == idioma]


# ............................................. #
# Consigna 5 Busqueda por ISBN
# ............................................. #
def buscar_y_subir_precio(catalogo):
    isbn = solicitar_isbn()
    libro = busqueda_por_isbn(catalogo, isbn)
    if libro:
        print("Libro encontrado:")
        print(libro)
        aumentar_10(libro)
    else:
        print("No se encontró el libro en cuestión")


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


# ............................................. #
# Consigna 6 Display Libros Genero Popular
# ............................................. #
def mostrar_genero_popular(catalogo):
    genero_popular = indice_maximo(contar_x_genero(catalogo))
    catalogo = sub_catalogo_genero(catalogo, genero_popular)
    ordenar_por_precio(catalogo)
    catalogo = catalogo[::-1]
    print("\nListado de libros del genero más popular ({}):".format(genero_to_str(genero_popular)))
    for libro in catalogo:
        print(libro)


def sub_catalogo_genero(catalogo, genero):
    return [libro for libro in catalogo if libro.genero == genero]


def ordenar_por_precio(catalogo):
    n = len(catalogo)
    h = 1
    while h <= n // 9:
        h = 3 * h + 1

    while h > 0:
        for j in range(h, n):
            y = catalogo[j]
            k = j - h
            while k >= 0 and y.precio < catalogo[k].precio:
                catalogo[k + h] = catalogo[k]
                k -= h
            catalogo[k + h] = y
        h //= 3


# ............................................. #
# Consigna 7 Consulta Combo
# ............................................. #
def solicitar_codigos():
    print("A continuación, deberá introducir los códigos de los libros que sean de su interes.")
    exit_flag = False
    codigos = []
    while not exit_flag:
        print("Hasta ahora se han cargado {} codigos.".format(len(codigos)))
        isbn = input("Por favor ingres un código ISBN válido. Ingrese 0 para salir")
        if isbn == "0":
            exit_flag = True
        elif validar_isbn(isbn):
            codigos.append(isbn)
        else:
            print(isbn_error_msj(isbn))
    return codigos


def consulta_combo(catalogo):
    codigos = solicitar_codigos()

    # Busca libros en el catalogo segun isbn
    encontrados = []
    no_encontrados = []
    for codigo in codigos:
        libro = busqueda_por_isbn(catalogo, codigo)
        if libro:
            encontrados.append(libro)
        else:
            no_encontrados.append(codigo)

    # Avisa que libros no se encontraron
    if len(no_encontrados) > 0:
        print("No se encontraron libros que correspondan a los siguientes {} códigos:".format(len(no_encontrados)))
        for codigo in no_encontrados:
            print(codigo)

    # Trabaja con los libros que se encontraron
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
