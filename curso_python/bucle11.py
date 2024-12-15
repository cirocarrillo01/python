#bucle while

"""while 1 == 1:
    print("ayuda estoy atrapado en un bucle")
    break"""

nombre = ""

while not nombre or len(nombre) == 0:
    nombre = input("ingresa tu nombre: ")


print("nombre " + nombre)