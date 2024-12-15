# cadenas de python, modificar

from ast import Slice


nombre = "ciro antonio carrillo mendoza"# se cuenta desde cero, c=0 i=1 r=3 o=4

primer_nombre = nombre[:4]#sustraer nombre
apellido = nombre[13:22]#sustraer apellido
nombre_dos = nombre[0::2]# salto
nombre_invertido = nombre[::-1] # nombre invertido

print(primer_nombre)
print(apellido)
print(nombre_dos)
print(nombre_invertido)
print(len(nombre))

#eliminar una parte del texto

website = "https://www.udemy.com/"
slice_obj = slice(12,-5)# funcion de corte o objeto de corte
sitio = website[slice_obj]

print(sitio)

