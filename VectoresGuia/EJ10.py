
def primer_aparicion(array, numero):
    for i in range(len(array)):
        if array [i] == numero:
            return i
    return -1

numeros = [7, 8, 10, 1, 5, 11]
buscar = int(input("ingrese el numero a buscar: "))

posicion = primer_aparicion(numeros, buscar)

if posicion != -1:
    print(f"el numero {buscar} aparece primero en la posicion {posicion} ")
else:
    print(f"el numero {buscar} no se encuentra en la array ")