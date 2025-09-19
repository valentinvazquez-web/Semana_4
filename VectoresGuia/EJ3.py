
vec_reales = [0] * 6
suma_reales = 0

for i in range (len(vec_reales)):
    vec_reales[i] = float(input("Ingresar numero: "))

for i in range (len(vec_reales)):
    print(f"Numero{i + 1}: {vec_reales[i]}")

for i in range (len(vec_reales)):
    suma_reales += vec_reales[i]

promedio_reales = suma_reales / len (vec_reales)

print(f"El promedio es de: {promedio_reales}")