#metodos

nombre="primeRo"
print(len(nombre))# cuenta los caracteres
nombre="segundo"
print(nombre.find("o"))# busca la ubicacion del caracter
nombre="tercero"
print(nombre.capitalize())#la primera letra en mayuscula
nombre="cuarTo"
print(nombre.upper())#todo en mayuscula
nombre="quinTo"
print(nombre.lower())#todo en minuscula
nombre="Sexto4 si"
print(nombre.isalnum())#pregunta si es un digito o no en el str, True o False
nombre="septimo d"
print(nombre.isalpha())#pregunta o analiza si tiene un caracter especial en el str, True o False
nombre="octavo intento"
print(nombre.count("o"))#cntamos cuantos caracteres hay
nombre="noveno"
print(nombre.replace("v","d"))# ramplaza un caracter por otro

#caracteristica extra
print(nombre*3)