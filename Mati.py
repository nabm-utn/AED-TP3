def menu_de_opciones():
    opcion = None
    menu = 'Menú de opciones\n' \
           '----------------\n' \
           '1.) Generar y cargar el catálogo de libros a la venta\n' \
           '2.) Ver el catálogo en orden alfabético\n' \
           '3.) Ver la cantidad de libros por género y conocer el género con mayor cantidad de libros\n' \
           '4.) Verificar el libro más caro para un idioma\n' \
           '5.) Aumentar 10% el precio de un libro (se ingresa el ISBN)\n' \
           '6.) Consultar listado de libros del género más numeroso, ordenado de mayor a menor precio\n' \
           '7.) Consultar existencia de libros escolares solicitados para el ciclo lectivo y obtener precio por grupo\n' \
           '8.) Finalizar programa'
    while opcion != '8':
        print(menu)
        opcion = input('Ingrese opción: ')
        if opcion == '1':
            opcion1()
        elif opcion == '2':
            opcion2()
        elif opcion == '3':
            opcion3()
        elif opcion == '4':
            opcion4()
        elif opcion == '5':
            opcion5()
        elif opcion == '6':
            opcion6()
        elif opcion == '7':
            opcion7()
        elif opcion == '8':
            confirmacion = input('Seleccionó finalizar programa. ¿Está seguro que desea salir? s/n: ')
            if confirmacion == 's' or confirmacion == 'S':
                print('Gracias por utilizar este programa. Hasta pronto.')
            else:
                opcion = None
        else:
            print('La opción ingresada no es válida')


def validar_positivos(n, minimo):
    if minimo <= n:
        return True
    else:
        return False


def validar_genero(gen):
    if 0 <= gen <= 9:
        return True
    else:
        return False


def validar_idioma(idi)
    if 0 < idi < 6:
        return True
    else:
        return False


def generar_catalogo(n):
catalogo = n * [None]
for i in range(n):
    cod = input('Código de Identificación (ISBN): ')
        while not validar_isbn(cod):
            print('Error. ISBN no válido, ingrese otro.')
            cod = input('Código de Identificación (ISBN): ')
    tit = input('Título: ')
    gen = int(input('Género (0-9): '))
        while not validar_genero(gen):
            print('Error. Los códigos para identificar el género van del 0 al 9, ingrese otro.')
            gen = int(input('Género (0-9): '))
    idi = int(input('Idioma (1-5): '))
        while not validar_idioma(idi):
            print('Error. Los códigos para identificar idioma van del 1 al 5, ingrese otro.')
            idi = int(input('Idioma (1-5): '))
    pre = round(float(input('Precio: $')), 2)
        while not validar_positivos(pre,0):
            print('Error, para cargar el precio no se admiten valores negativos, ingrese otro valor.')
            pre = round(float(input('Precio: $')), 2)
    catalogo[i] = Libro(cod, tit, gen, idi, pre)


def buscar_y_subir_precio(catalogo, isbn):
    for i in range(len(catalogo)):
        if isbn == catalogo[i].isbn:
            print('Libro encontrado')
            # Acá hay que mostrar los datos del libro no sé como hacerlo
            confirma = input('Presione s para subir precio 10%')
            if confirma == 's' or confirma == 'S':
                catalogo[i].precio *= 1.1
                print('El nuevo precio es: $', catalogo[i].precio)
            # no me queda claro que pasa si presiona otra tecla que no sea S
        else:
            print('Libro no encontrado')


def contar_x_genero(catalogo, generos, opcion):
    contador = 10 * [0]
    mayor = 0
    for i in range(len(catalogo)):
        contador[catalogo[i].genero] +=1
    for i in range(len(contador)):
        if opcion == 3:
            print('el género', generos[i], 'tiene', contador[i], 'libros')
        if contador[i] > mayor:
            mayor = generos[i], i, contador[i]
    if opcion == '3':
        print('El género con mayor cantidad de libros es:', mayor[0])
    elif opcion == '6':
        return mayor


def ordenar_mayor_a_menor(vector):
    pass


def consultar_libros_de_un_genero(catalogo, mayor):
    genero_popular = [None] * mayor[2]
    g = 0
    for i in range(len(catalogo)):
        if catalogo[i].genero == mayor[1]:
            genero_popular[g] = catalogo[i]
            g += 1
    ordenar_mayor_a_menor(genero_popular)
    for i in range(len(genero_popular)):
        print(genero_popular[i])

