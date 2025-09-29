
MAX = 10
lista_alumnos = [""] * MAX
lista_libros = [0] * MAX
lista_comentarios = [""] * MAX

# ---------- Función de validación de ingreso de textos -----------
def ingresar_texto(mensaje):
    texto = ""
    while texto == "":
        texto = input(mensaje)
        if texto == "":
            print("No puede quedar en blanco.")
    
    return texto


# ------------ Función para validar la cantidad de libros de 1 a 20 ----------
def ingresar_libros(mensaje):
       while True:
        libros = int(input(mensaje))
        if 1 <= libros <= 20:
            return libros
        else:
            print("Debe ingresar una cantidad de libros entre 1 y 20")
            
        

#-----------------------------Carga de datos---------------------------
def ingresar_datos(lista_alumnos, lista_libros, lista_comentarios, cantidad):
    while cantidad < MAX:
        print(f"------ Alumno {cantidad + 1} ------")
        lista_alumnos[cantidad] = ingresar_texto("Ingrese su nombre: ")
        lista_libros[cantidad] = ingresar_libros("Ingrese la cantidad de libros leídos (1-20): ")
        lista_comentarios[cantidad] = ingresar_texto("Ingrese un comentario: ")

        cantidad += 1

        continuar = input("Desea continuar cargando alumnos? (s/n): ").lower()
        if continuar != "s":
            break
    return cantidad

# ------------ Mostrar datos ---------------
def mostrar_datos(alumnos, libros, comentarios, cantidad):
    if cantidad == 0:
        print("No hay datos cargados...")
        return
    suma = 0

    print("----- Alumnos cargados -----")
    for i in range(cantidad):
        print(f"{i + 1}. {alumnos[i]} - Libros leídos: {libros[i]} - Comentario: {comentarios[i]}")
        suma += libros[i]
    promedio = suma / cantidad
    print(f"Promedio de libros leídos: {promedio:.2f}")

# ---------------------------- Ordenar listas -------------------------
def ordenar_por_libros(alumnos, libros, comentarios, cantidad):
    if cantidad == 0:
        print("No hay datos para ordenar...")
        return

    for i in range(cantidad - 1):
        for j in range(cantidad - 1 - i):
            if libros[j] < libros[j + 1]:
                libros[j], libros[j + 1] = libros[j + 1], libros[j]
                alumnos[j], alumnos[j + 1] = alumnos[j + 1], alumnos[j]
                comentarios[j], comentarios[j + 1] = comentarios[j + 1], comentarios[j]

    print(" ----- Alumnos ordenados por libros -----")
    for i in range(cantidad):
        print(f"{i + 1}. {alumnos[i]} - Libros leídos: {libros[i]} - Comentario: {comentarios[i]}")


# --------- Programa principal ------------------
cantidad = 0

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Ingresar datos de alumnos")
    print("2. Mostrar cantidad de libros leidos y comentarios")
    print("3. Ordenar alumnos por cantidad de libros leidos")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cantidad = ingresar_datos(lista_alumnos, lista_libros, lista_comentarios, cantidad)
    elif opcion == "2":
        mostrar_datos(lista_alumnos, lista_libros, lista_comentarios, cantidad)
    elif opcion == "3":
        ordenar_por_libros(lista_alumnos, lista_libros, lista_comentarios, cantidad)
    elif opcion == "4":
        print("Gracias por dejarnos su informacion.")
        break
    else:
        print("Opción inválida, intente nuevamente.")