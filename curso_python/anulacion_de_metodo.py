###--------------###

class Animal:
    
    def comer(self):
        print('Este animal esta comiendo')

class Conejo(Animal):
    def comer (self):
        print('este conejo esta comiendo una zanahoria')


conejo = Conejo()
conejo.comer()
