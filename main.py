"""
Este es el programa principal. A continuación voy a armar una estructura base a partir de comentarios.
"""
from logic import actualizar_catalogo, mostrar_libros_ordenados, conteo_y_genero_popular, libro_mas_caro_por_idioma
from logic import buscar_y_subir_precio, mostrar_genero_popular, consulta_combo


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
            actualizar_catalogo(catalogo)
        elif opcion == '2':
            mostrar_libros_ordenados(catalogo)
            input("...")
        elif opcion == '3':
            conteo_y_genero_popular(catalogo)
            input("...")
        elif opcion == '4':
            libro_mas_caro_por_idioma(catalogo)
            input("...")
        elif opcion == '5':
            buscar_y_subir_precio(catalogo)
            input("...")
        elif opcion == '6':
            mostrar_genero_popular(catalogo)
            input("...")
        elif opcion == '7':
            consulta_combo(catalogo)
            input("...")
        elif opcion == '8':
            confirmacion = input('Seleccionó finalizar programa. ¿Está seguro que desea salir? s/n: ')
            if confirmacion == 's' or confirmacion == 'S':
                print('Gracias por utilizar este programa. Hasta pronto.')
            else:
                opcion = None
        else:
            print('La opción ingresada no es válida')


if __name__ == "__main__":
    catalogo_principal = []
    menu_de_opciones(catalogo_principal)
