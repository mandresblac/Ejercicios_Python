import math

print("Progrma de calculo de raiz cuadrada")
numero= int(input("Intorduce un número por favor: "))

intentos= 0

while numero<0:
    print("No se puede hallar la raiz de un número negativo")
    if intentos == 2:
        print("Has consumido demasiados intentos. El programa a finalizado")
        break

    numero= int(input("Intorduce un número por favor: "))
    if numero<0:
        intentos +=1

if intentos<2:
    solucion= math.sqrt(numero)
    print(f"La raiz cuadrada de {str(numero)} es {str(solucion)}")

