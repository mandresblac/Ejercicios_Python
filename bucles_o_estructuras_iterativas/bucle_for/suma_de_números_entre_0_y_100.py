# Escribir un programa que muestre la sumatoria de todos los números entre el 0 y el 100.

total=0
for i in range(101):
    total += i # Esto es igual a: total = total + i
print("Sumatoria total: {}".format(total))

#Luego cambiar el programa para que sume unicamente los números que son multiplos de 3.

total=0
for i in range(101):
    if i % 3 == 0:
            total += i # Esto es igual a: total = total + i
print("Sumatoria total: {}".format(total))
