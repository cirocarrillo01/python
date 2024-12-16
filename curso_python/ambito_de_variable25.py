#ambito de variable
nombre = "carrillo" #variable global
def mostrar_nombre ():
    nombre = "ciro"#variable local solo esta entre la funcion
    print(nombre)

mostrar_nombre()
print(nombre)