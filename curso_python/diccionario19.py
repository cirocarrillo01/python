#diccionario

from multiprocessing.sharedctypes import Value

capitales = {"EE.UU": "washington",
           "argentina":"buenos aires",
           "chile":"santiago de chile",
           "brasil":"brasilia",
}#clave y valor. int, float, str

capitales.update({"alemania":"berlin"})
capitales.pop("EE.UU")
#capitales.clear()
#print(capitales.get["chile"])
#print(capitales.keys())
#print(capitales.values())
#print(capitales.items())

for key, value in capitales.items():
    print(key,value)




