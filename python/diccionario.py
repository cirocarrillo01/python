midiccionario={"alemania":"berlin","colombia":"bogota","francia":"paris","argentina":"buenos aires"}
midiccionario["italia"]="lisboa"#agregar
print(midiccionario)
midiccionario["italia"]="roma"#modificar
print(midiccionario)

del midiccionario["alemania"]#eliminar
print(midiccionario)

#asignar claves con una tupla
mitupla=["mexico","venezuela","cuba","ecuador","chile"]
midiccionario1={mitupla[0]:"ciudad de mexico",mitupla[1]:"caracas",mitupla[2]:"habana",mitupla[3]:"guayaquil",mitupla[4]:"santiago de chile"}
print(midiccionario1["venezuela"])

midiccionario={23:"jordan","nombre":"michael","equipo":"chicago","anillos":{"temporadas":[1991,1993,1993,1996,1997,1998]}}
print(midiccionario.keys())
print(midiccionario.values())
print(midiccionario.items())
print(len(midiccionario)) #valores
print(midiccionario)


