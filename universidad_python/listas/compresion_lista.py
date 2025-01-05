# ----- compresion de lista -----
print(' ----- compresion de lista ----- ')

# una lista con el cuadrado de cada numero
numeros = [1,2,3,4,5]
cuadrados = [x**2 for x in numeros]
print(cuadrados)

# lista de numeros pares
numeros = range(10+1)
pares = [x for x in numeros if x % 2 == 0 ]
print(pares)

#lista de numeros impares
numeros = range(10+1)
impares = [x for x in numeros if x % 2 == 1]
print(impares)

#lista saludando a cada nombre
nombres= ['ana','jeronimo','carlos']
saludando = [f'hola {nombre}' for nombre in nombres]
print(saludando)