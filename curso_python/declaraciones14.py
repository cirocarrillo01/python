#break, continuos y pass

#----- break -------

"""nombre = ""
while True:# romper bucle con break
    nombre = input("ingrese nombre: ")
    if nombre != "":
        break"""
# ------ continue -------
telefono = "524-789-631"
for i in telefono: #
    if i == "-":
        continue# encuentra dicho elemento continua
    print(i,end="")

# ------- pass -------
for i in range(1,21):
    if i == 13:
        pass# actua como marcador de posicion
    else:
        print(i)