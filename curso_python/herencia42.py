class Animal:

    vivo = True

    def comer(self):
        print('esta comiendo')

    def dormir(self):
        print('esta durmiendo')

class Conejo(Animal):
    def correr(self):
        print('corriendo!')

class Pez(Animal):
    def nadar(self):
        print('nadando!')

class Halcon(Animal):
    def volar(self):
        print('volando!')

conejo = Conejo()
pez = Pez()
halcon = Halcon()

pez.nadar()
conejo.correr()
halcon.volar()