#funciones

"""def saludo(nombre2):
    print("hola " + nombre2)
    print("que tengas un buen dia")

nombre = input("ingrese un nombre: ")
saludo(nombre)"""

def saludo(primer_nombre,apellido,edad):
    print("hola " + primer_nombre + " " + apellido)
    print("Tienes " + str(edad) + " años")
    print("que tengas un buen dia")

nombre = input("ingrese un nombre: ")
saludo(nombre, "carrillo",24)
