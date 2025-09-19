
def buscar_valor():
    
    vec_numeros = [0] * 10  

    
    for i in range(10):
        vec_numeros[i] = int(input(f"Ingrese un número para la posición {i}: "))

    
    buscado = int(input("\nIngrese el número a buscar: "))

    
    encontrado = False
    for i in range(len(vec_numeros)):
        if vec_numeros[i] == buscado:
            print(f"El número {buscado} se encuentra en la posición {i}.")
            encontrado = True
            break  

    if not encontrado:
        print(f"El número {buscado} no se encuentra en el array ")

buscar_valor()