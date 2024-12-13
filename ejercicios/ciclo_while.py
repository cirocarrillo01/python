dinero = 50
while dinero > 0:
    print("puedo comprar")
    dinero=dinero-10
contador = 1
while contador <=10:
    print(contador)
    contador+=1



contraseña="hola"
contraseñaUsuario=input("ingrese contraseña: ")
contador=0
while contraseña!= contraseñaUsuario:#compara la contraseña en la condicion
    contador+=1
    print("contraseña incorrecta")
    print(contador)
    contraseñaUsuario=input("ingrese contraseña: ")#pide de nuevo la contraseña
    if (contador>=2):#se empieza a contar desde 0=1 1=2 2=3
        print("usted supero el limite de intentos fallidos")
        print("intente mas tarde")
        break

if (contraseña==contraseñaUsuario):
    print("bienvenido al sistema")