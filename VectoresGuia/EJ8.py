def comparar_arrays():
    array1 = [0] * 5
    array2 = [0] * 5

    print("Cargar primer array:")
    for i in range(5):
        array1[i] = int(input(f"Elemento {i}: "))

    print("Cargar segundo array:")
    for i in range(5):
        array2[i] = int(input(f"Elemento {i}: "))

    iguales = True
    for i in range(5):
        if array1[i] != array2[i]:
            iguales = False
            break

    if iguales:
        print("Los arrays son iguales.")
    else:
        print("Los arrays no son iguales.")

comparar_arrays()