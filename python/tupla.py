mitupla=("ciro",19,2,1995)#tupla en parentesis
milista=list(mitupla)#convertir tupla en lista
print(milista)

milista1=["ciro",19,2,1995]#lista en corchetes
mitupla1=tuple(milista1)#convertir lista en tupla
print(mitupla1)

print("ciro" in mitupla)# esta ciro en la tupla
print(mitupla.count(19))# cuentas veces esta 19 en a tupla

nombre, dia, mes, agno=mitupla#desempacado de tupla
print(nombre)
print(dia)
print(mes)
print(agno)