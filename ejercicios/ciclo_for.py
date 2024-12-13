for i in range(10):
    print(i)
    #desde una ubicacion
print("desde una ubicacion")

for j in range(5,10):#de 5 hasta 10
    print(j)
print("cuenta regresiva")

for h in range(100,0,-1):#cuenta regresiva
    print(h)

print("")
suma_a=0
for i in range(1,6):#suma en un rango
    suma_a=suma_a+i
    print("el resultado de la suma ",suma_a)
print("el resultado final es: ",suma_a)

print("con input")
valor=int(input("hasta donde quiero sumar: "))
suma=0
for i in range(1,valor+1):#suma en un rango
    suma=suma+i
    print("el resultado de la suma ",suma)
print("el resultado final es: ",suma)

#imprime los primeros 20 multiplos de numero
n=int(input("ingrese un numero para ver sus primeros 20 multiplos: "))
for i in range(1,6):
    print(n*i)

for j in range(10):
    print(j)
    if (j==4):
        break
