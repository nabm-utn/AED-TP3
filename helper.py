def validar_positivo(n, minimo=0, maximo=0):
    if maximo and minimo < maximo:
        return minimo <= n <= maximo
    return minimo <= n


def input_positivo(msj, minimo=0, maximo=0, is_float=False):
    n = float(input(msj))
    while not validar_positivo(n, minimo, maximo):
        warning = "Debe ingresar un numero positivo"
        if minimo:
            warning += " mayor a {}".format(minimo)
        if maximo:
            warning += " menor a {}".format(maximo)
        print(warning)
        n = float(input(msj))
    if is_float:
        return n
    else:
        return int(n)


def validar_genero(genero):
    return 0 <= genero <= 9


def validar_idioma(idioma):
    return 1 <= idioma <= 5


def indice_maximo(vector):
    """
    Devuelve el índice del valor máximo de un vector. Si hay más de un valor máximo retorna solo el primero
    Es equivalente (aunque con peor performance) al builtin max()
    :param vector: un iterable con valores numéricos
    :return: el indice del valor mayor del vector provisto
    """
    mayor = vector[0]
    mayor_index = 0
    index = 0
    for elemento in vector[1:]:
        index += 1
        if elemento > mayor:
            mayor = elemento
            mayor_index = index
    return mayor_index


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
