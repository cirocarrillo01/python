#detencion de archivos

import os

path = '/home/mendoza/Público/python'
#puedes ubicarte con la termina usando find ~ -name "nombre del archivo"
if os.path.exists(path):
    print("esa ubicacion existe")
    if os.path.isfile(path): #identificar para archivo
        print("es un archivo")
    elif os.path.isdir(path): #identificar para carpeta o directorio
        print("es un directorio")
else:
    print("esa ubucacion no existe")
#mlocate es otra opcion
""" sudo apt install mlocate
sudo updatedb
en terminal:
locate 'nombre del archivo' """