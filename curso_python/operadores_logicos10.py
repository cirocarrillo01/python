#operadores logicos and, or y not

temperatura = int(input("cual es la temperatura afuera: "))

# las dos condiciones debe cumplirse o ser verdadera en and
if temperatura >= 0 and temperatura <= 30:
    print("la temperatura esta bien hoy :D")
# una de las dos condiciones deben ser verdadera en or
elif temperatura <0 or temperatura > 0:
    print(" la temperatura esta mal hoy")
    
temperatura = int(input("cual es la temperatura afuera: "))
print("con operador logico not aplicado")
# operador logico invierte verdadera a falso o alrevez
# las dos condiciones debe cumplirse o ser verdadera en and
if not temperatura >= 0 and temperatura <= 30:
    print(" la temperatura esta mal hoy")
# una de las dos condiciones deben ser verdadera en or
elif not temperatura <0 or temperatura > 0:
    print("la temperatura esta bien hoy :D")
