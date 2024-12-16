#arg, es un parametro que enpaquetaa todos los argumeno en una tupla

def suma(*args):#*arg argumento enpaquetado en una tupla
    suma = 0
    for i in args:
        suma += i
    return suma

print(suma(1,5,3,4,5,6))


#cambiar dato

def suma1(*args):#*arg argumento enpaquetado en una tupla
    suma1 = 0
    cosas = list(args)#convierte en lista
    cosas[0] = 0#remplaza un valor de la lista
    for i in cosas:
        suma1 += i
    return suma1

print(suma1(1,5,3,4,5,6))