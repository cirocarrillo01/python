milista=["a","b","c","d"]
milista.append("e")#lo agrega al final
milista.insert(6,"f")#insertar un elemento en un posicion de la lista
milista.extend(["g","h","i"])#agrega otra lista
milista2=["j","k","l","m"]

milista3=milista+milista2
print(milista3)

milista.remove("d")#elimina la d de la lista
milista.pop()#elimina en la ubicacion asignada
print(milista[:])
print(milista.index("e"))# 0 es 1

print("f" in milista) #imprime siesta en la lista, true
print(milista[2])