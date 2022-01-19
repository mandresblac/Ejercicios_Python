#imprimir todos los números entre el 100 y el 199.

print(" Programa que imprime todos los números entre el 100 y el 199 ".center(136,"-"))

num=int(input("Inserte un número entre 100 y 199: "))

while True:
    if num >= 101 and num <= 199:
        for i in range(100, num + 1, 1):
            print(i, end=" ")
        print()
        break
    else:
        print("ERROR, numero fuera de rango")
        num=int(input("Inserte un número entre 100 y 199: "))



