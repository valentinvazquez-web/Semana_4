titulos = [""] * 20
ejemplares = [0] * 20
cantidad_libros = 0

titulos [0] = "El señor de los anillos"
ejemplares [0] = 5

titulos [1] = "Orgullo y Prejuicio"
ejemplares [1] = 3

titulos [2] = "Los Juegos del Hambre"
ejemplares [2] = 7

titulos [3] = "Carrie"
ejemplares [3] = 0 #libro agotado

def cargar_libros(titulos, ejemplares, cantidad_libros): 
    while cantidad_libros < 20:
        titulo = input("Ingrese el titulo: ")
        if titulo == "":
            break
        copias = int(input("Ingrese la cantidad de ejemplares: "))
        titulos [cantidad_libros] = titulo
        ejemplares[cantidad_libros] = copias
        cantidad_libros = cantidad_libros + 1
    return cantidad_libros

def mostrar_catalogo(titulos, ejemplares, cantidad_libros):
    if cantidad_libros == 0:
        print("no hay libros cargados")
    else: 
        for i in range(cantidad_libros):
            print(titulos[i], ejemplares [i], "copias")

def consultar_disponibilidad(titulos, ejemplares, cantidad_libros):
    buscado = input("ingrese titulo a consultar: ")
    encontrado= False
    for i in range(cantidad_libros):
        if titulos[i].lower() == buscado.lower():
            print("El libro", titulos[i], "tiene", ejemplares[i], "copias")
            encontrado = True
    if not encontrado: 
        print("No está en el catálogo")

def listar_agotados(titulos, ejemplares, cantidad_libros):
    ninguno = True
    for i in range(cantidad_libros):
        if ejemplares[i] == 0:
            print(titulos[i], "agotado")
            ninguno = False
    if ninguno:
        print("no hay libros agotados o sin stock")

def agregar_titulo(titulos, ejemplares, cantidad_libros):
    if cantidad_libros >= 20:
        print("No se pueden cargar mas libros")
    else: 
        titulo = input("Ingrese un nuevo titulo: ")
        copias = int(input("Ingrese la cantidad de ejemplares: "))
        titulos[cantidad_libros] = titulo
        ejemplares[cantidad_libros] = copias
        cantidad_libros = cantidad_libros +1
    return cantidad_libros

def actualizar_ejemplares(titulos, ejemplares, cantidad_libros): 
    buscado = input("Ingrese titulo a actualizar: ")
    actualizado = False
    for i in range(cantidad_libros):
        if titulos[i].lower() == buscado.lower():
            nuevo = int(input("ingrese una nueva cantidad de ejemplares: "))
            ejemplares[i] = nuevo
            print("cantidad actualizada")
            actualizado = True
    if not actualizado: 
        print("No se encontró el titulo")

opcion = 0
while opcion != 7:
    print("Menu")
    print("1. Cargar titulos y ejemplares")
    print("2. Mostrar el catalogo completo")
    print("3. Consultar disponibilidad")
    print("4. Listar titulos agotados")
    print("5. Agregar un nuevo titulo")
    print("6. Actualizar ejemplares(prestamo/devolución)")
    print("7. Salir")

    opcion = int(input("Elija una opción: ")) 

    if opcion == 1:
        cantidad_libros = cargar_libros(titulos, ejemplares, cantidad_libros)
    elif opcion == 2:
        mostrar_catalogo(titulos, ejemplares, cantidad_libros)
    elif opcion == 3:
        consultar_disponibilidad(titulos, ejemplares, cantidad_libros)
    elif opcion == 4: 
        listar_agotados(titulos, ejemplares, cantidad_libros)
    elif opcion == 5:
        cantidad_libros = agregar_titulo(titulos, ejemplares, cantidad_libros)
    elif opcion == 6:
        actualizar_ejemplares(titulos, ejemplares, cantidad_libros)
    elif opcion == 7:
        print("Saliendo del sistema...")
    else: 
        print("Opcion no válida")