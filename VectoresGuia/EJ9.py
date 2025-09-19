
def reemplazar_pares():
    vec_numeros = [0] * 10
    for i in range(10):
        vec_numeros[i] = int(input(f"Ingrese el número para la posición {i}: "))

    for i in range(len(vec_numeros)):
        if vec_numeros[i] % 2 == 0:
            vec_numeros[i] = 0

    print("Array resultante:")
    for i in range(len(vec_numeros)):
        print(f"Posición {i}: {vec_numeros[i]}")

reemplazar_pares()