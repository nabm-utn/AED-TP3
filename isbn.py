from random import randrange


def validar_isbn(posible_isbn):
    if len(posible_isbn) != 13:
        return False

    grupos = posible_isbn.split("-")
    if len(grupos) != 4:
        return False
    for grupo in grupos:
        if len(grupo) < 1:
            return False

    c_cifras = 10
    total = 0
    for char in posible_isbn:
        if char.isnumeric():
            total += c_cifras * int(char)
            c_cifras -= 1
        elif char != "-":
            return False

    return not total % 11


def isbn_error_msj(posible_isbn):
    """
    Variacion de validar_isbn, retorna 0 si posible_isbn es válido, y sino retorna un codigo indicando el error.
    :param posible_isbn:
    :return: int entre 0 y 1
    """
    if len(posible_isbn) != 13:
        return "ISBN invalido, no tiene 13 caracteres"

    grupos = posible_isbn.split("-")
    if len(grupos) != 4:
        return "ISBN invalido, no tiene 4 grupos numéricos"
    for grupo in grupos:
        if len(grupo) < 1:
            return "ISBN invalido, un grupo numérico está vacío"

    c_cifras = 10
    total = 0
    for char in posible_isbn:
        if char.isnumeric():
            total += c_cifras * int(char)
            c_cifras -= 1
        elif char != "-":
            return "ISBN invalido, tiene caracteres distintos de números y guiones"

    if not total % 11:
        return "ISBN invalido, los digitos no respetan la regla de multiplicidad de 11"

    return "ISBN valido"


def generar_isbn():
    cifras = []
    total = 0
    # genera las primeras 8 cifras
    for c in range(8):
        cifra = randrange(10)
        cifras.append(cifra)
        total += (10-c) * cifra

    # genera la cifra 9
    resto = total % 11
    estocastico = randrange(1, 7)
    cifra_9 = (resto + estocastico) // 2
    cifras.append(cifra_9)
    total += 2*cifra_9

    # genera la cifra 10
    resto = total % 11
    if resto == 0:
        cifra_10 = 0
    elif resto == 1:
        cifras[-1] += 1
        cifra_10 = 9 - resto
    else:
        cifra_10 = 11 - resto
    cifras.append(cifra_10)

    len_grupos = [1, 1, 1, 1]
    for s in range(6):
        len_grupos[randrange(4)] += 1

    nuevo_isbn = ""
    contador = 0
    for grupo in range(4):
        for c in range(len_grupos[grupo]):
            nuevo_isbn += str(cifras[contador])
            contador += 1
        nuevo_isbn += "-"
    return nuevo_isbn[:-1]


if __name__ == "__main__":
    print("\n"+"="*20+"TESTS"+"="*20+"\n")

    # test para validar_isbn
    result1 = validar_isbn("84-8181-227-7")
    result2 = validar_isbn("74-8181-227-7")
    result3 = validar_isbn("94-8181-227-8")
    if (result1, result2, result3) != (True, False, True):
        print("validar_isbn: ERROR!")
    else:
        print("validar_isbn: PASS!")

    # test para generar_isbn
    errores = 0
    for i in range(10000):
        isbn = generar_isbn()
        if not validar_isbn(isbn):
            print("generar_isbn: ERROR! ||", isbn)
            errores += 1
    if not errores:
        print("generar_isbn: PASS!")
    else:
        print("{}% de errores...".format(errores / 100))
