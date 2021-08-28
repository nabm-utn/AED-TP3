# Funciones Generales
def validar_positivo(n, minimo=0, maximo=0):
    if maximo and minimo < maximo:
        return minimo <= n <= maximo
    return minimo <= n


def input_int_positivo(msj, minimo=0, maximo=0):
    n = int(input(msj))
    while not validar_positivo(n, minimo, maximo):
        warning = "Debe ingresar un numero entero positivo"
        if minimo:
            warning += " mayor a {}".format(minimo)
        if maximo:
            warning += " menor a {}".format(maximo)
        print(warning)
        n = int(input(msj))
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
    maximo = vector[0]
    maximo_index = 0
    index = 0
    for elemento in vector[1:]:
        if elemento > maximo:
            maximo = elemento
            maximo_index = index
        index += 1
    return maximo_index


def genero_to_str(genero):
    if not validar_genero(genero):
        return "genero desconocido"
    generos = ("Autoayuda", "Arte", "Ficción", "Computación", "Economía",
               "Escolar", "Sociedad", "Gastronomía", "Infantil", "Otros")
    return generos[genero]


def idioma_to_str(idioma):
    if not validar_idioma(idioma):
        return "idioma desconocido"
    idiomas = ("español", "ingles", "frances", "italiano", "otros")
    return idiomas[idioma-1]