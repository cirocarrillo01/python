#liminar archivos

import os
import shutil

path = 'prueba' #funciona con carpetas o archivos



try:
    #os.remove(path)#para archivos
    #os.rmdir(path)#para carpetas vacias
    shutil.rmtree(path)#elimina carpeta junto archivos, usar con preucacion
except FileNotFoundError:
    print("El archivo no se encontro!")
except PermissionError:
    print("No puedes eliminar esta carpeta")
except IsADirectoryError:
    print("Error, se produce comúnmente en situaciones donde se espera un archivo, pero se proporciona un directorio.")
except OSError:
    print("error, carpeta con contenido")
else:
    print(path + " fue eliminado!")
    
