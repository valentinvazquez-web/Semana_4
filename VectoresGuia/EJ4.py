
vec_numeros = [0] * 8

for i in range (len(vec_numeros)):
    vec_numeros[i] = int(input("Ingresar numero: "))

contador = 0
for i in range (len(vec_numeros)):
    if vec_numeros[i] > 100:
        contador += 1

print("La cantidad de números mayores a 100 es:", contador)