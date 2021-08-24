"""
Acá vamos a definir el "registro" (en realidad clase) Libro. También vamos a armar una
librería estandar con 30 (digo yo, charlable) libros para la parte 1.1 de main.py
"""
import random


class Libro:
    def __init__(self, isbn, titulo, genero, idioma, precio):
        self.isbn = isbn
        self.titulo = titulo
        self.genero = genero
        self.idioma = idioma
        self.precio = precio


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


def generar_isbn():
    cifras = []
    total = 0
    # genera las primeras 8 cifras
    for c in range(8):
        cifra = random.randrange(10)
        cifras.append(cifra)
        total += (10-c) * cifra

    # genera la cifra 9
    resto = total % 11
    estocastico = random.randrange(1, 7)
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
        len_grupos[random.randrange(4)] += 1

    isbn = ""
    contador = 0
    for grupo in range(4):
        for c in range(len_grupos[grupo]):
            isbn += str(cifras[contador])
            contador += 1
        isbn += "-"
    return isbn[:-1]


def auto_fill(n=30):
    posibles_generos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    posibles_idiomas = [1, 2, 3, 4, 5]
    posibles_titulos = ["Mi planta de mandarina-limón",
                        "Ratero y yo",
                        ]

    catalogo = []
    for c in range(n):
        isbn = generar_isbn()
        titulo = random.choice(posibles_titulos)
        genero = random.choice(posibles_generos)
        idioma = random.choice(posibles_idiomas)
        precio = random.randrange(300) + round(random.random(), 2)
        libro = Libro(isbn, titulo, genero, idioma, precio)
        catalogo.append(libro)
    return catalogo


if __name__ == "__main__":
    # test para validar_isbn
    result1 = validar_isbn("84-8181-227-7")
    result2 = validar_isbn("74-8181-227-7")
    result3 = validar_isbn("94-8181-227-8")
    if (result1, result2, result3) != (True, False, True):
        print("Error: validar_isbn")

    # test para generar_isbn
    print("\n"+"="*20+"TESTS"+"="*20+"\n")
    errores = 0
    for i in range(10000):
        isbn = generar_isbn()
        if not validar_isbn(isbn):
            print("Error: generar_isbn ||", isbn)
            errores += 1
    print("{}% de errores...".format(errores/100))
