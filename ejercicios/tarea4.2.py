# Función para convertir un número decimal a binario
def decimal_a_binario(decimal):# opcion 3 en la lista
    binario = 0
    potencia = 1
    while decimal > 0:
        resto = decimal % 2
        binario += resto * potencia
        decimal //= 2
        potencia *= 10
    return binario

# Función para convertir un número binario a decimal
def binario_a_decimal(binario):# opcion 1 en la lista
    decimal = 0
    potencia = 0
    while binario > 0:
        digito = binario % 10
        decimal += digito * (2 ** potencia)
        binario //= 10
        potencia += 1
    return decimal

# Función para convertir un número decimal a hexadecimal
def decimal_a_hexadecimal(decimal):# opcion 4 en la lista
    valores_hex = "0123456789ABCDEF"
    hexadecimal = ""
    while decimal > 0:
        resto = decimal % 16
        hexadecimal = valores_hex[resto] + hexadecimal
        decimal //= 16
    return hexadecimal

# Función para convertir un número hexadecimal a decimal
def hexadecimal_a_decimal(hexadecimal):# opcion 2 en la lista
    valores_hex = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                   'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    decimal = 0
    potencia = 0
    hexadecimal = hexadecimal.upper()
    for digito in reversed(hexadecimal):
        decimal += valores_hex[digito] * (16 ** potencia)
        potencia += 1
    return decimal

# Función para convertir un número hexadecimal a binario
def hexadecimal_a_binario(hexadecimal):# opcion 6 en la lista
    decimal = hexadecimal_a_decimal(hexadecimal)
    return decimal_a_binario(decimal)

# Función para convertir un número binario a hexadecimal
def binario_a_hexadecimal(binario):# opcion 5 en la lista
    decimal = binario_a_decimal(binario)
    return decimal_a_hexadecimal(decimal)

# Menú de opciones
menu = """
Selecciona el tipo de conversión que deseas realizar:
1 - Decimal a Binario
2 - Binario a Decimal
3 - Decimal a Hexadecimal
4 - Hexadecimal a Decimal
5 - Hexadecimal a Binario
6 - Binario a Hexadecimal
7 - Salir
"""

# Ciclo principal del programa
while True:
    print(menu)
    opcion = int(input("Ingresa la opción de conversión disponibles: "))

    if opcion == 7:
        print("programa finalizado")
        break
    if opcion == 1:  # Decimal a Binario
        decimal = int(input("Ingresa el número decimal: "))
        resultado = decimal_a_binario(decimal)
        print(f"El número decimal {decimal} en binario es: {resultado}")

    elif opcion == 2:  # Binario a Decimal
        binario = int(input("Ingresa el número binario: "))
        resultado = binario_a_decimal(binario)
        print(f"El número binario {binario} en decimal es: {resultado}")

    elif opcion == 3:  # Decimal a Hexadecimal
        decimal = int(input("Ingresa el número decimal: "))
        resultado = decimal_a_hexadecimal(decimal)
        print(f"El número decimal {decimal} en hexadecimal es: {resultado}")

    elif opcion == 4:  # Hexadecimal a Decimal
        hexadecimal = input("Ingresa el número hexadecimal: ")
        resultado = hexadecimal_a_decimal(hexadecimal)
        print(f"El número hexadecimal {hexadecimal} en decimal es: {resultado}")

    elif opcion == 5:  # Hexadecimal a Binario
        hexadecimal = input("Ingresa el número hexadecimal: ")
        resultado = hexadecimal_a_binario(hexadecimal)
        print(f"El número hexadecimal {hexadecimal} en binario es: {resultado}")

    elif opcion == 6:  # Binario a Hexadecimal
        binario = int(input("Ingresa el número binario: "))
        resultado = binario_a_hexadecimal(binario)
        print(f"El número binario {binario} en hexadecimal es: {resultado}")

    else:
        print("Opción no válida. Por favor, elige una opción válida.")

    # Preguntar si quiere hacer otra conversión
    continuar = input("¿Quieres hacer otra conversión? (s/n): ")
    if continuar != 's':
        print("programa finalizado")
        break