"""
Este es el programa principal. A continuación voy a armar una estructura base a partir de comentarios.
"""
import libro

# ============================================= #
# Parte 0 Funciones Auxiliares
# ============================================= #


def validar_positivo(n, minimo):
    if minimo <= n:
        return True
    else:
        return False


def validar_genero(genero):
    if 0 <= genero <= 9:
        return True
    else:
        return False


def validar_idioma(idioma):
    if 1 <= idioma < 5:
        return True
    else:
        return False


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
    catalogo_principal += libro.auto_fill(30)

# ............................................. #
# Parte 1.2 Generación Manual
# ............................................. #


def generar_libro_manual():
    isbn = input('Código de Identificación (ISBN): ')
    while not libro.validar_isbn(isbn):
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
    return libro.Libro(isbn, titulo, genero, idioma, precio)


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

# ............................................. #
# Parte 2.3 Libro mas caro segun idioma
# ............................................. #
# -> Vector de registros de un dado idioma
# -> encontrar el mayor y mostrarlo


def sub_catalogo_idioma(catalogo=catalogo_principal, idioma=1):
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

# ............................................. #
# Parte 2.5 Display Libros Genero Popular
# ............................................. #
# -> Usar codigo de 2.2
# -> Generar un vectorcito de libros del genero
# -> Ordenarlo
# -> Mostrarlo

# ............................................. #
# Parte 2.6 Consulta Combo
# ............................................. #
# -> Usar codigo de 2.4
# -> Acumulador de precio
# -> Mostrar resultados
