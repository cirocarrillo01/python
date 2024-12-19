#moviendo archivos en python

import os

origen = 'copy.txt' # puede copiar una carpeta tambien
destino = '/home/mendoza/Público/python/python'#ruta a enviar

try:
    if os.path.exists(destino):
        print("ya hay un archivo en el destino")
    else:
        os.replace(origen, destino)
        print(origen + " fue movido")
except FileNotFoundError:
    print(origin + " no fue encontrado!")


