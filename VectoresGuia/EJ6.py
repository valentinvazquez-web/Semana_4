
def mayoryposicion():
    
    vec_numeros = [0] * 7  
    
    for i in range(7):
        vec_numeros[i] = int(input(f"Ingrese el número {i}: "))

    mayorNum = vec_numeros[0]
    posicion = 0

    for i in range(1, len(vec_numeros)):
        if vec_numeros[i] > mayorNum:
            mayorNum = vec_numeros[i]
            posicion = i

    print(f"El número mayor es {mayorNum} y se encuentra en la posición {posicion}.")

mayoryposicion()