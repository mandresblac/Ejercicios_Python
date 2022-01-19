# Ejercicio 1
'''
edad = int(input("Inserta una edad: "))

while edad <= 18:
    print("Felicidades, tienes {}".format(str(edad)))
    edad += 1
'''

#Ejercicio 2

edad = int(input("Inserta una edad: "))

while edad <= 18:
    if edad % 2 == 0:
        continue # La palabra continue hace que el programa solo imprima la siguiente linea si la edad insertada es un número impar
    print("Felicidades, tienes {}".format(str(edad)))

