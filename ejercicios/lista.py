"""lista son estructuras de datos que me permiten almacenar informacion de diferentes tipos, numero, cadenas y objetos"""

numeros=[1,2,3,4,5,6,7,8]
numeros.insert(8,9)
numeros[1]=30
numeros.remove(5)
numeros.pop(7)#elimina en la ubicion
nombres=["juan","ines","maria","pedro"]
listamixta=[1,"hola",48,"juan","maria","pedro",20]
listaVacia=[]
listaVacia.append("lucas")
print(listaVacia)

print(numeros)

for numero in numeros:
    print(numeros)
    if numero%2==0:
        numeros[numero]=0
print(numeros)