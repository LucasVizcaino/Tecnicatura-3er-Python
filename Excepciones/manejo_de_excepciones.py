import NumerosIgualesExcepciones
resultado = None


#Atrapamos una excepcion   
try:
    a = int(input("Digite un numero: "))
    b = int(input("Digite un numero: "))
    resultado = a/b
    if a == b:
        raise NumerosIgualesExcepciones("Son iguales")
except Exception as e:
    print(f"El error es: {e}")
else:
    print("No arrojo ninguna excepcion")
finally:
    print("Esto se va a ejecutar siempre")
        
print(f"El resultado es {resultado}")