"""
Este es el programa principal. A continuación voy a armar una estructura base a partir de comentarios.
"""
import libro

# ============================================= #
# Parte 0 Funciones Auxiliares
# ============================================= #

# ............................................. #
# Parte 0.1 Menú de Opciones General
# ............................................. #
# => Hacible

# ............................................. #
# Parte 0.2 Validación ISBN
# ............................................. #
# => HECHO

# ............................................. #
# Parte 0.3 Ordenar arreglo
# ............................................. #

#to_string() (decodificar idioma y genero)

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
# Hacible

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

