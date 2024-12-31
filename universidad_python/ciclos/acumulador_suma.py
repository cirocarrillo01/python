# ------  acumulador suma ------------------
print('----- acumulador suma -----')
MAXIMO = 5
numero = 1
acumulador_suma = 0
while numero <= MAXIMO:
    #imprimir lo que se va a sumar
    print(f'acumulador_suma + numero: {acumulador_suma} + {numero}')
    acumulador_suma += numero
    numero += 1

    #imprimir el resultado de la suma parcial
    print(f'Suma parcial acumulada: {acumulador_suma}\n')

print(f'Resultado de la suma: {acumulador_suma}')

