# Ciclo for
# programa que pide un número mayor que 0 e imprime en patalla todos los números empezando desde 1 hasta el número insertado.

num=int(input("Inserte un número: "))

while True:
    if num > 0:
        for i in range(1, num + 1, 1):
            print(i, end=" ")
        print()
        break
    else:
        num <= 0
        print("Error, numero fuera de rango")
        num=int(input("Inserte un número: "))

