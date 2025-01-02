#-------- juego de adivinacion -------------
'''comentario:
'''
# ----- constante ------------------------------------
from random import randint
numero_secreto = randint(1,50)
intentos = 0
numero = 0
INTENTOS_MAXIMOS = 5
# ----- ciclos ---------------------------------------
print('----- juego de adivinaza ------')
while numero != numero_secreto and intentos < INTENTOS_MAXIMOS:
    numero = int(input('ingresa numero del 1 al 50: '))
    print(f'numero de intento: {intentos}')
    if numero > numero_secreto:
        print(f'numero {numero} es mayor, que el secreto')
    elif numero < numero_secreto:
        print(f'numero {numero} es menor, que el secreto')
    intentos += 1
if numero == numero_secreto:
    print(f'felicidades adivinaste el numero secreto en el intento: {intentos}')
else:
    print(f'lo siento, has agotado tus intentos maximos: {INTENTOS_MAXIMOS}')
    print(f'El numero secreto era: {numero_secreto}')