# Ejercicio de funcion suma

def suma(num1, num2):
    "Esta es una funcion que suma"
    resultado = num1 + num2
    return resultado

num1= int(input("Inserte un número: "))
num2= int(input("Inserte otro número: "))

print("La suma de {} + {} es igual a {}".format(num1, num2, suma(num1, num2)))

