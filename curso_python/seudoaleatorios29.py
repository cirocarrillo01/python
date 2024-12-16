#modulo random
import random

x = random.randint(1,6)
y = random.random()

print(y)

mi_lista = ["piedra", "papel", "tijeras"]
z = random.choice(mi_lista)

cartas = ["1","2","3","4","5","6","7","8","9","j","q","k","a"]
random.shuffle(cartas)

print(cartas)