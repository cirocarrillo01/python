valor=int(input("ingrese un numero entero del 8 al 3: "))#
"""if(valor==0):
    print("muy mal")
elif valor==1:
    print("mal")
elif valor==2:
    print("bien")
elif valor==3:
    print("muy bien")
else:
    print("opcion no es validad")
   """
match valor:
    case 0:
        print("muy mal")
    case 1:
        print("mal")
    case 2:
        print("bien")
    case 3:
        print("muy bien")
    case _:
        print("opcion no valida")