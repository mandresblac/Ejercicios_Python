#Imprimir los números entre el 5 y el 20, saltando de tres en tres.

print(" Programa que imprime los números entre el 5 y el 20, saltando de tres en tres ".center(136, "-"))

num=int(input("Inserte un número entre 6 y 20: "))

while True:
    if num >= 6 and num < 21:
        for i in range(6, num + 1 , 3):
            print(i, end=" ")
        print()
        break
    else:
        print("ERROR; número fuera de rango.")
        num=int(input("Inserte un número entre 6 y 20: "))


