"""
Acá vamos a definir el "registro" (en realidad clase) Libro. También vamos a armar una
librería estandar con 30 (digo yo, charlable) libros para la parte 1.1 de main.py
"""


class Libro:
    def __init__(self, isbn, titulo, genero, idioma, precio):
        self.isbn = isbn
        self.titulo = titulo
        self.genero = genero
        self.idioma = idioma
        self.precio = precio

    def __str__(self):
        base = "[{}] {} | {} - {} | ${}"
        generos = ("Autoayuda", "Arte", "Ficción", "Computación", "Economía",
                   "Escolar", "Sociedad", "Gastronomía", "Infantil", "Otros")
        idiomas = ("español", "ingles", "frances", "italiano", "otros")
        return base.format(self.isbn, self.titulo, generos[self.genero], idiomas[self.idioma-1], self.precio)
