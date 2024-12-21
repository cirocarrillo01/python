#herencia multi nivel

class Organismo:
    vivo = True

class Animal(Organismo):
    def comer(self):
        print('Este anima esta comiendo ...')

class Perro(Animal):
    def ladrar(self):
        print('Este perro esta ladrando ...')
        
perro = Perro()
perro.ladrar()