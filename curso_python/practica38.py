#practica

import random

lista =['piedra','papel','tijera']
while True:
    computadora=random.choice(lista)
    jugador = None
    
    while jugador not in lista:
        jugador= input('¿piedra, papel o tijera? ').lower()

    if jugador == computadora:
        print('computadora: ', computadora)
        print('jugador: ', jugador)
        print('empate!')
    elif jugador == 'piedra':    
        if computadora == 'papel':
            print('computadora: ', computadora)
            print('jugador: ', jugador)
            print('perdite!')
        if computadora == 'tijera':
            print('computadora: ', computadora)
            print('jugador: ', jugador)
            print('ganaste!')
    elif jugador == 'papel':    
        if computadora == 'tijera':
            print('computadora: ', computadora)
            print('jugador: ', jugador)
            print('perdite!')
        if computadora == 'piedra':
            print('computadora: ', computadora)
            print('jugador: ', jugador)
            print('ganaste!')
    elif jugador == 'tijera':    
        if computadora == 'piedra':
            print('computadora: ', computadora)
            print('jugador: ', jugador)
            print('perdite!')
        if computadora == 'papel':
            print('computadora: ', computadora)
            print('jugador: ', jugador)
            print('ganaste!')
            
    jugar_de_nuevo = input('¿jugar de nuevo? (si/no)').lower()

    if jugar_de_nuevo != 'si':
        break 

print('adios!!!')