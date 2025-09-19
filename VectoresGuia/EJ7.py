
def invertir_array():
    vec_numeros = [0] * 6
    for i in range(6):
        vec_numeros[i] = int(input(f"Ingrese el número para la posición {i}: "))
    
    print("Array invertido:")
    for j in range(5, -1, -1):
        print(vec_numeros[j])

invertir_array()