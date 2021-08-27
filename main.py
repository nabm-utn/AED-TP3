"""
Este es el programa principal. A continuación voy a armar una estructura base a partir de comentarios.
"""
from libro import Libro
from helper import validar_positivo, input_int_positivo, validar_genero, validar_idioma, maximo, genero_to_str
from isbn import validar_isbn
from auto import auto_fill


test = False


# ............................................. #
# Parte 0.1 Menú de Opciones General
# ............................................. #
def menu_de_opciones(catalogo):
    opcion = None
    menu = """
Bienvenido a PyBooks!
-----------------------------------------------------
Menú de opciones   |  Libros disponibles: {}
-----------------------------------------------------
1.) Generar y cargar el catálogo de libros a la venta
2.) Ver el catálogo en orden alfabético
3.) Ver la cantidad de libros por género y conocer el género con mayor cantidad de libros
4.) Verificar el libro más caro para un idioma
5.) Aumentar 10% el precio de un libro (se ingresa el ISBN)
6.) Consultar listado de libros del género más numeroso, ordenado de mayor a menor precio
7.) Consultar existencia de libros escolares solicitados para el ciclo lectivo y obtener precio por grupo
8.) Finalizar programa"""
    while opcion != '8':
        print(menu.format(len(catalogo)))
        opcion = input('Ingrese opción: ')
        if opcion == '1':
            generar_actualizar_catalogo(catalogo)
            input("...")
        elif opcion == '2':
            mostrar_libros_ordenados(catalogo)
            input("...")
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
# Parte 0.3 Slicing y Ordenamiento del catalogo
# ............................................. #
def sub_catalogo_idioma(catalogo, idioma):
    return [libro for libro in catalogo if libro.idioma == idioma]


def sub_catalogo_genero(catalogo, genero):
    return [libro for libro in catalogo if libro.genero == genero]


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


# ============================================= #
# Consigna 1 Generación del vector de registros.
# ============================================= #
catalogo_principal = []


def generar_actualizar_catalogo(catalogo):
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


# ............................................. #
# Parte 1 Generación Automática
# ............................................. #
# Esto de acá abajo es placeholder para las pruebas. Despues se quita a a la mergas...
def generar_catalogo_automatico():
    n = input_int_positivo("Ingrese la cantidad de libros a generar (0 para cancelar): ")
    return auto_fill(n)


# ............................................. #
# Parte 2 Generación Manual
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


def generar_catalogo_manual():
    catalogo = []
    n = input_int_positivo("Ingrese la cantidad de libros a generar (0 para cancelar): ")
    for i in range(n):
        print("\nLibro {} de {}".format(i+1, n))
        catalogo.append(generar_libro_manual())
    return catalogo


if __name__ == "__main__" and test:
    generar_actualizar_catalogo(catalogo_principal)
    [print(libro) for libro in catalogo_principal]


# ............................................. #
# Consigna 2 Display General
# ............................................. #
# -> Ordenar el arreglo alfabéticamente por titulo
# -> Mostrar todos los libros con genero e idioma decodificados
def mostrar_libros_ordenados(catalogo):
    ordenar_por_titulo(catalogo)
    print("Estos son los libros disponibles")
    for libro in catalogo:
        print(libro)


if __name__ == "__main__" and test:
    print("="*60+"\nTest Consigna 2\n")
    mostrar_libros_ordenados(catalogo_principal)


# ............................................. #
# Consigna 3 Popularidad de Genero
# ............................................. #
# -> Vector de Conteo
def contar_x_genero(catalogo):
    contador = 10 * [0]
    for libro in catalogo:
        contador[libro.genero] += 1
    return contador


def display_x_genero(contador):
    for i in range(len(contador)):
        print("El genero {} contiene: {:02d} libros".format(genero_to_str(i), contador[i]))


def conteo_y_genero_popular(catalogo):
    contador = contar_x_genero(catalogo)
    display_x_genero(contador)
    genero_popular = maximo(contador)
    cantidad_popular = contador[genero_popular]
    print("El género más popular es {} con un total de {} libros".format(genero_popular, cantidad_popular))


# ............................................. #
# Consigna 4 Libro mas caro segun idioma
# ............................................. #
# -> Vector de registros de un dado idioma
# -> encontrar el mayor y mostrarlo
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


if __name__ == "__main__" and test:
    print("="*60+"\nTest Consigna 4\n")
    for idioma in range(1, 6):
        libro_mas_caro_idioma(catalogo_principal, idioma)


# ............................................. #
# Consigna 5 Busqueda por ISBN
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
    if not validar_isbn(isbn):
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
# Consigna 6 Display Libros Genero Popular
# ............................................. #
# -> Usar codigo de Consigna 3
# -> Generar un vectorcito de libros del genero
# -> Ordenarlo
# -> Mostrarlo
def mostrar_genero_popular(catalogo):
    genero_popular = maximo(contar_x_genero(catalogo))
    catalogo = sub_catalogo_genero(catalogo, genero_popular)
    ordenar_por_precio(catalogo)
    catalogo = catalogo[::-1]
    print("\nListado de libros del genero más popular ({}):".format(genero_to_str(genero_popular)))
    for libro in catalogo:
        print(libro)


if __name__ == "__main__" and test:
    print("="*60+"\nTest parte 2.5\n")
    mostrar_genero_popular(catalogo_principal)


# ............................................. #
# Consigna 7 Consulta Combo
# ............................................. #
# -> Usar codigo de Consigna 5
# -> Acumulador de precio
# -> Mostrar resultados
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
            print("Codigo inválido")
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


if __name__ == "__main__":
    menu_de_opciones(catalogo_principal)