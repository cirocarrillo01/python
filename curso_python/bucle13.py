#bucle anidados

fila = int(input("¿cuantas filas?"))
columna = int(input("¿cuantas columnas?"))
simbolo = input(" ingrese simbolo: ")

for i in range (fila):
    for j in range (columna):
        print(simbolo, end="")
    print(" ")
