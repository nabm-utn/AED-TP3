# Funciones Generales
def validar_positivo(n, minimo):
    return minimo <= n


def input_int_positivo(msj):
    n = -1
    while not validar_positivo(n, 0):
        n = input(msj)
        try:
            n = int(n)
        except ValueError:
            print("Debe ingresar un numero entero positivo")
            n = -1
    return n


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
        if elemento > maximo:
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


# Funciones asociadas a ISBN
