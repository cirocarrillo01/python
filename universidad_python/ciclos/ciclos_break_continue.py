# ----- ciclos break y continue ------------------------
print(' ----- ciclos break y continue ------ ')

# Ejemplo con break
print('palabra break')
for numero in range(1, 10):
    if numero % 2 == 0: # numero par
        print(numero)
        break # salimos del ciclo inmediato

# Ejemplo con continue
print()
print('palabra continue')
for numero in range(1, 10):
    if numero % 2 == 1: # numero impar
        continue
    print(numero) # numeros pares