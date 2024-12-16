#kwargs

def hola(**kwargs):
    print("hola " + kwargs["nombre"] + " " + kwargs["apellido"])

hola(nombre="ciro", apellido="carrillo", segundo_nombre="antonio")

def hola (**kwargs):## dos * por delante
    print("hola", end = " ")
    for clave, valor in kwargs.items():
        print(valor, end = " ")

hola(titulo= "señor", nombre="ciro", apellido="carrillo",segundo_nombre="python")




