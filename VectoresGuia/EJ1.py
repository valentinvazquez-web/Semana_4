
vec_numerosE = [0] * 5

print(vec_numerosE)

for i in range (len(vec_numerosE)):
    vec_numerosE[i] = int(input("Ingresar numero: "))

for i in range (len(vec_numerosE)):
    print(f"Numero {i + 1}: {vec_numerosE[i]}")