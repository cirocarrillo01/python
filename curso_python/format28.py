#str.format()=
str_1 = "leche"
str_2 = "casar"



#print("arroz con leche me quiero casar")
#print("arroz con leche " + str_1 + " me quiero casar " + str_2)
#print("arroz con {} me quiero {}".format("leche","casar"))
#es importanet el orden
#print("arroz con {1} me quiero {0}".format("leche","casar"))
#es importanet el orden, se organizo con indice invertido
#print("arroz con {} me quiero {}".format(str_1="leche",str_2="casar"))
#con los indicen con las palabras clave

#texto = "arroz con {} me quiero {}"
#print(texto.format(str_1, str_2))

#nombre = "ciro"
#print("hola, mi nombre es {}".format(nombre))
#print("hola, mi nombre es {:10}. mucho gusto :D".format(nombre))#deja un espacio de 10 caracterescon el [:10]
#print("hola, mi nombre es {:<10}. mucho gusto :D".format(nombre))#
#print("hola, mi nombre es {:>10}. mucho gusto :D".format(nombre))#
#print("hola, mi nombre es {:^10}. mucho gusto :D".format(nombre))#



numero = 3.14159
print("el numero pi es: {:.2f}".format(numero))
numero = 1000
print("el numero pi es: {:b}".format(numero))#binario
numero = 1000
print("el numero pi es: {:o}".format(numero))
numero = 1000
print("el numero pi es: {:x}".format(numero))
numero = 1000
print("el numero pi es: {:e}".format(numero))
