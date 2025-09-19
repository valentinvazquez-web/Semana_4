
vec_numeros = [0] * 10
suma_numeros = 0

for i in range (len(vec_numeros)):
    vec_numeros[i] = int(input("Ingresar numero: "))

for i in range (len(vec_numeros)):
    print(f"Numero {i + 1}: {vec_numeros[i]}")

for i in range (len(vec_numeros)):
    suma_numeros += vec_numeros[i]

print(f"La suma detodos los numeros da: {suma_numeros}")