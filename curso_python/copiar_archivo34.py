#copiar archivos en python
#copyfile()
#copy()
#copy2()

import shutil
# Copiar el archivo 'texto1.txt' a 'copy.txt' en el mismo directorio
shutil.copyfile('texto1.txt', 'copy.txt')

# Usando copy()
shutil.copy('texto1.txt', 'copy.txt')

# Usando copy2()
shutil.copy2('texto1.txt', 'copy.txt')

#en otro directorio
shutil.copyfile('texto1.txt', '/home/mendoza/Público/python/copy.txt')

"""
Explicación de las Funciones:

    shutil.copyfile(src, dst): Copia el contenido del archivo src al archivo dst. Si dst ya existe, se sobrescribirá.

    shutil.copy(src, dst): Similar a copyfile(), pero también copia los metadatos del archivo (como permisos).

    shutil.copy2(src, dst): Igual que copy(), pero intenta preservar más metadatos del archivo original.
"""

