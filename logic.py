from libro import Libro
from helper import input_positivo, validar_genero, validar_idioma, indice_maximo, genero_to_str, idioma_to_str
from isbn import validar_isbn, isbn_error_msj
from auto import auto_fill


# ============================================= #
# Consigna 1 Generación del vector de registros.
# ============================================= #
def actualizar_catalogo(catalogo):
    menu = """
Libros en el catálogo: {}
Por favor seleccione el tipo de carga a realizar
1.) Manual
2.) Automática
3.) Volver al Menú Principal"""
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


def solicitar_titulo():
    titulo = input('Título: ')
    while len(titulo) == 0:
        titulo = input('Título (No puede estar vacío): ')
    return titulo


def solicitar_genero():
    msj = 'Género (0: Autoayuda, 1:Arte, 2: Ficción, 3: Computación, 4: Economía, \n' \
          '5: Escolar, 6: Sociedad, 7: Gastronomía, 8: Infantil , 9: Otros): '
    genero = int(input(msj))
    while not validar_genero(genero):
        print('Error. Los códigos para identificar el género van del 0 al 9, ingrese otro.')
        genero = int(input(msj))
    return genero


def solicitar_idioma():
    idioma = int(input('Seleccione un idioma (1: español, 2: inglés, 3: francés, 4:italiano, 5:otros): '))
    while not validar_idioma(idioma):
        print('Error. Los códigos para identificar idioma van del 1 al 5, ingrese otro.')
        idioma = int(input('Idioma (1-5): '))
    return idioma


def solicitar_precio():
    precio = input_positivo("Precio: $", is_float=True)
    return round(precio, 2)


def generar_libro_manual():
    isbn = solicitar_isbn()
    titulo = solicitar_titulo()
    genero = solicitar_genero()
    idioma = solicitar_idioma()
    precio = solicitar_precio()
    return Libro(isbn, titulo, genero, idioma, precio)


# ............................................. #
# Consigna 2 Display General
# ............................................. #
def mostrar_libros_ordenados(catalogo):
    ordenar_por_titulo(catalogo)
    print("\nEstos son los libros disponibles")
    print("{:^15} | {:^11} | {:^8} | {:^10} | {:^33}".format("ISBN", "Género", "Idioma", "Precio", "Título"))
    print("-"*90)
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
    print()
    contador = contar_x_genero(catalogo)
    display_x_genero(contador)
    genero_popular = indice_maximo(contador)
    cantidad_popular = contador[genero_popular]
    genero_popular = genero_to_str(genero_popular)
    print("\nEl género más popular es {} con un total de {} libros".format(genero_popular, cantidad_popular))


def contar_x_genero(catalogo):
    contador = 10 * [0]
    for libro in catalogo:
        contador[libro.genero] += 1
    return contador


def display_x_genero(contador):
    for i in range(len(contador)):
        print("Hay {:02d} libros para el género {}".format(contador[i], genero_to_str(i)))


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
    print("")
    isbn = solicitar_isbn()
    libro = busqueda_por_isbn(catalogo, isbn)
    if libro:
        print("Libro encontrado:")
        print(libro)
        aumentar_10(libro)
    else:
        print("No se encontró un libro con el ISBN especificado")


def busqueda_por_isbn(catalogo, isbn):
    for libro in catalogo:
        if libro.isbn == isbn:
            return libro
    return False


def aumentar_10(libro):
    confirma = input("Desea aumentar el precio del libro en un 10%? (s/n): ")
    if confirma == "s" or confirma == "S":
        libro.precio *= 1.1
        print("El nuevo precio es: ${}".format(round(libro.precio, 2)))
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
    print("\n{:^15} | {:^11} | {:^8} | {:^10} | {:^33}".format("ISBN", "Género", "Idioma", "Precio", "Título"))
    print("-"*90)
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
    print("\nA continuación, deberá introducir los códigos de los libros que sean de su interes.")
    exit_flag = False
    codigos = []
    while not exit_flag:
        print("\nHasta ahora se han cargado {} codigos.".format(len(codigos)))
        isbn = input("Por favor ingres un código ISBN válido. Ingrese 0 para finalizar la carga:\n")
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
        print("\n{} de los códigos ingresados no están en el catálogo:".format(len(no_encontrados)))
        for codigo in no_encontrados:
            print(codigo)

    # Trabaja con los libros que se encontraron
    if len(encontrados) > 0:
        print("\nLibros encontrados en el catálogo: {}".format(len(encontrados)))
        print("\n{:^15} | {:^11} | {:^8} | {:^10} | {:^33}".format("ISBN", "Género", "Idioma", "Precio", "Título"))
        print("-" * 90)
        precio_total = 0
        for libro in encontrados:
            print(libro)
            precio_total += libro.precio
        print("-"*90)
        print("El precio por todos los libros disponibles es de: ${}".format(round(precio_total, 2)))
    else:
        print("En este momento el catálogo no contiene ningún libro de los solicitados.")
