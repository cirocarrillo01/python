#leer contenido
#debe estar almacenado en la misma carpeta o directorio
try:
    with open('texto1.txt') as file:#file es la variable donde se almacena
        print(file.read())
except FileNotFoundError:
    print("el archivo no fue encontrado")


"""print(file.closed)
#si esta abierdo dira False y si esta cerrado dira True
"""