#Programa que muestra si el número insertado es par o impar

n=int(input("Inserte un numero entero: "))

if n % 2 == 0:
    print("{} es un número par.".format(n))
else:
    print(f"{n} es un número impar.")

