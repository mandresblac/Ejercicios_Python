# importamos la clase math
import math

def calculaRaiz(num1):
    if num1<0:
        raise ValueError("El número no puede ser negativo") #Lanzamos una excepcion
    else:
        return math.sqrt(num1)

op1=int(input("Introduce un número: "))

try:
    print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print("ErrorDeNumeroNegativo")

print("Programa terminado")
