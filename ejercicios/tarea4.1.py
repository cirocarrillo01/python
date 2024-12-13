#Desarrolle su ejercicio aquí.
conversion_factores = [
    1000, # kilometros a metros
    0.01, # centimetros a metros
    0.62, # kilometros por hora a millas por hora
    20,   # nota en Educatic a nota en Canvas
    0.05, # nota en Canvas a nota en Educatic
    0.001,# milimetro a centimetros cubicos
    4470, # dolar a peso colombiano(actualizado manualmente) "que no suba mas el dolar :V "
    0.00022,# peso colombiano a dolar(actualizado manualmente)
    0.45, # libra a kilogramo
    17987539.67 # minuto luz a kilometro
]

unidades_de_medida = [
    "metros",
    "metros",
    "millas por hora",
    "nota en Canvas",
    "nota en Educatic",
    "centimetros cubicos",
    "pesos colombianos",
    "dolares",
    "kilogramos",
    "kilometros"
]

unidades_de_ingreso = [
    "kilometros",
    "centimetros",
    "kilometros por hora",
    "nota en Educatic",
    "nota en Canvas",
    "mililitros",
    "dolares (USA)",
    "pesos colombianos",
    "libras",
    "minutos luz"
]

# menu de opciones
menu = """
selecciona el tipo de conversion:
0	- Kilómetro a metro
1	- Centímetro a metro
2	- Kilómetro por hora a millas por hora
3	- Nota en Educatic a nota en Canvas
4	- Nota en Canvas a nota en Educatic
5	- Mililitro a centímetro cúbico
6	- Dólar (USA) a peso colombiano
7	- Peso colombiano a dólar (USA)
8	- Libra a kilogramo
9	- Minuto luz a kilómetro
10 - salir
"""

def valor_conversion():
    unidad_ingreso = unidades_de_ingreso[opcion]
    conversion=unidades_de_medida[opcion]
    valor = float(input(f"ingrese el valor de {unidad_ingreso} a convertir: "))
    resultado = (valor * conversion_factores[opcion])
    #resultado de conversion
    print(f"el resultado de la conversion es: {resultado} {conversion}")
valor=0
conversion=0

while True:
    print(menu)
    opcion= int(input("ingrese su opcion: "))
    if opcion >= 0 and opcion <= 9:
        valor_conversion()
    if opcion ==10:
        print("fin del programa")
        break
    if opcion < 0 or opcion >= 11:
        print("opcion invalida")
    continuar=input("¿quieres cntinuar?(s/n)")
    if continuar != "s":
        print("fin del programa")
        break