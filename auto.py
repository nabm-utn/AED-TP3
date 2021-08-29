from random import choice, randrange, random
from isbn import generar_isbn
from libro import Libro

posibles_generos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
posibles_idiomas = [1, 2, 3, 4, 5]
posibles_titulos = ["Mi planta de mandarina-limón",
                    "Ratero y yo",
                    "A Game of Phones",
                    "La vuelta al muno en 90 días",
                    "Le petit-roi",
                    "A todo gas 7, desafío kyoto",
                    "The Time of Wheel",
                    "La banana mecánica",
                    "Las crónicas de Marmia",
                    "Jarry Qotter and the chamber of mysteries",
                    "Don Quejote y su mancha",
                    "Mati Fierro",
                    "El código DiCaprio",
                    "50 shades of green",
                    "La selfie de Dorian Gray",
                    "El Alef",
                    "Los Juegos del Sueño",
                    "Convergente",
                    "99 años de compañía",
                    "El romance en los tiempos del Dengue",
                    "El Puente",
                    "Inés del alma tuya",
                    "El perro lazarillo de Tomas",
                    "1894",
                    "Vanidad y Discriminación",
                    "El guardian entre la cebada",
                    "Sierras Borrascosas",
                    "Brave Old World",
                    "The Lord Of the Rims",
                    "A Tale of two towns",
                    "Catch 66",
                    "El extraño caso del Señor Jekyll y el Doctor Hyde",
                    "Crimen y Recompensa",
                    "La Homereada",
                    "Charly y la fábrica de maní con chocolate",
                    "El conde de luxemburgo",
                    "El arte de la Paz",
                    "La Madrina",
                    "El virrey que me amó",
                    ]


def auto_fill(n=30):
    catalogo = []
    for c in range(n):
        isbn = generar_isbn()
        titulo = choice(posibles_titulos)
        genero = choice(posibles_generos)
        idioma = choice(posibles_idiomas)
        precio = randrange(300) + round(random(), 2)
        catalogo.append(Libro(isbn, titulo, genero, idioma, precio))
    return catalogo


if __name__ == "__main__":
    print("test para auto_fill")
    my_catalogo = auto_fill(15)
    for libro in my_catalogo:
        print(libro)
