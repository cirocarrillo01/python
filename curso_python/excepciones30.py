#excepciones
try:
    numerador = int(input("ingresa un numero: "))
    denominador = int(input("ingrese un numero: "))
    resultado = numerador / denominador
except ZeroDivisionError as e:
    print(e)
    print("no puede dividir por cero!")
except ValueError as e:
    print(e)
    print("por favor, ingrese solo numeros")
except Exception as e:
    print(e)
    print("algo salio mal!")
else:
    print(resultado)
finally:
    print("esto se ejecutara siempre")
