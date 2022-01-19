#Ejercicios bucle while.

"""
i = 1
while i <= 3:
    print(i)
    i += 1 #i = i + 1
print("Programa terminado.")
"""

"""
numero = int(input("Escriba un número positivo: "))
while numero < 0:
    print("¡Ha escrito un número negativo! Inténtelo de nuevo.")
    numero = int(input("Escriba un número positivo: "))
print("Gracias por su colaboración.")
"""

"""
total = 0
nro = int(input("Ingrese un número: "))
while nro != 0:
    total += nro
    nro = int(input("Número: "))
print("Fin del programa.")
"""

"""
positivos = 0
n = int(input("Número (0 para terminar): "))
while n != 0:
    if n> 0:
        positivos += 1
    n = int(input("Número (0 para terminar): "))
print("Cantidad de positivos:", positivos)
"""


def main():
    print("SUMA DE NÚMEROS")
    numero = int(input("Escriba un número: "))
    suma = 0
    while numero >= 0:
        suma += numero
        numero = int(input("Escriba otro número: "))
    print()
    print(f"La suma de los números positivos introducidos es {suma}.")


if __name__ == "__main__":
    main()