#indexacion

nombre = "ciro carrillo"

"""if nombre[0].islower():
    nombre = nombre.capitalize()
"""

primer_nombre = nombre[0:4].upper()
apellido = nombre[5:].lower()
ultimo_caracter = nombre[-1]

print(primer_nombre)
print(apellido)
print(ultimo_caracter)