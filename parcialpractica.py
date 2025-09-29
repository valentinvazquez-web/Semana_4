
MAX = 10  # Máximo de participantes

# Crear listas vacías
def lista_nombres():
    return [""] * MAX

def lista_puntajes():
    return [0] * MAX

def lista_comentarios():
    return [""] * MAX

# Pedir texto no vacío
def pedir_texto(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato != "":
            return dato
        print("No puede estar vacío.")

# Revisar si es número
def es_numero(texto):
    if texto == "":
        return False
    for c in texto:
        if c not in "0123456789":
            return False
    return True

# Pedir número dentro de un rango
def pedir_numero(mensaje, minimo, maximo):
    while True:
        dato = input(mensaje).strip()
        if es_numero(dato):
            num = int(dato)
            if minimo <= num <= maximo:
                return num
        print(f"Ingrese un número entre {minimo} y {maximo}.")

# Ingresar datos de participantes
def cargar_participantes(nombres, puntajes, comentarios, cantidad):
    while cantidad < MAX:
        print(f"\nParticipante {cantidad+1}")
        nombres[cantidad] = pedir_texto("Nombre: ")
        puntajes[cantidad] = pedir_numero("Puntuación (1-10): ", 1, 10)
        comentarios[cantidad] = pedir_texto("Comentario: ")
        cantidad += 1

        seguir = input("¿Desea ingresar otro? (s/n): ").lower()
        if seguir == "n":
            break
    return cantidad

# Mostrar participantes y promedio
def mostrar_participantes(nombres, puntajes, comentarios, cantidad):
    if cantidad == 0:
        print("\nNo hay datos cargados.")
        return
    print("\n--- Lista de Participantes ---")
    suma = 0
    for i in range(cantidad):
        print(f"{i+1}. {nombres[i]} - {puntajes[i]} - {comentarios[i]}")
        suma += puntajes[i]
    print(f"Promedio de puntuaciones: {suma/cantidad:.2f}")

# Ordenar participantes por puntuación (ascendente)
def ordenar_participantes(nombres, puntajes, comentarios, cantidad):
    for i in range(cantidad-1):
        for j in range(cantidad-1-i):
            if puntajes[j] > puntajes[j+1]:
                puntajes[j], puntajes[j+1] = puntajes[j+1], puntajes[j]
                nombres[j], nombres[j+1] = nombres[j+1], nombres[j]
                comentarios[j], comentarios[j+1] = comentarios[j+1], comentarios[j]
    print("\n--- Lista Ordenada ---")
    mostrar_participantes(nombres, puntajes, comentarios, cantidad)

# Función principal
def main():
    nombres = lista_nombres()
    puntajes = lista_puntajes()
    comentarios = lista_comentarios()
    cantidad = 0

    while True:
        print("\n--- Menú Encuesta ---")
        print("1. Ingresar participantes")
        print("2. Mostrar participantes y promedio")
        print("3. Ordenar por puntuación")
        print("4. Salir")
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            cantidad = cargar_participantes(nombres, puntajes, comentarios, cantidad)
        elif opcion == "2":
            mostrar_participantes(nombres, puntajes, comentarios, cantidad)
        elif opcion == "3":
            ordenar_participantes(nombres, puntajes, comentarios, cantidad)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()