'''
#Programa para hallar el perimetro y area de un cuadrado.
#Autor: Manuel Blanco
#fecha: 05/Octubre/2020

#Encabezado del programa.
print("¡Vamos a hallar el perimetro y area de un cuadrado!")

#Peticion de datos.
valor = float(input("Inserta el largo (en metros) y pulsa enter: "))

#Calculos.
perimetro = valor * 4
area = valor * valor

#Impresion de resultados por pantalla.
print(f"El perimetro es: {round(perimetro, 2)} metros.")
print(f"El area es: {round(area, 2)} M2.")
'''

'''
#Programa para hallar el area de un triangulo.
#Autor: Manuel Blanco
#fecha: 05/Octubre/2020

#Encabezado del programa.
print("¡Vamos a hallar el area de un triangulo!")

#Peticion de datos.
base = int(input("Inserta la base del triangulo (en metros), luego oprime enter: "))
altura = int(input("Inserta la altura del triangulo (en metros), luego oprime enter: "))

#Calculos
area = (base * altura) / 2

#Impresion de resultados por pantalla.
print(f"El area del triangulo es: {round(area, 2)} M2. ", end="")
print("Gracias por usar el programa. ¡Adiós!")
'''

'''
#Programa para hallar el perimetro y area de un rectangulo.
#Autor: Manuel Blanco
#fecha: 05/Octubre/2020

#Encabezado del programa.
print("¡Vamos a hallar el perimetro y area de un rectangulo!")

#Peticion de datos.
largo = float(input("Inserta la altura (en metros), luego oprime la tecla enter: "))
ancho = float(input("Inserta el anchura (en metros), luego oprime la tecla enter: "))

#Calculos
perimetro = ((largo * 2) + (ancho * 2))
area = largo * ancho

#Impresion de resultados por pantalla.
print(f"El perimetro del rectangulo es: {round(perimetro, 2)} ml.")
print(f"El area del rectangulo es: {round(area, 2)} m2. ")
print("Gracias por usar el programa. ¡Adiós!")
'''

'''
#Programa para hallar el volumen de una esfera.
#Autor: Manuel Blanco
#fecha: 05/Octubre/2020

#importando libreria math
from math import pi

#Encabezado del programa.
print("¡Vamos a hallar el volumen de una esfera!")

#Peticion de datos.
radio = float(input("Inserta un número, luego oprime la tecla enter: "))

#Calculos.
volumen = 4 / 3  * pi * radio**3

#Impresion de resultados por pantalla.
print(f"El volumen de la esfera es: {volumen}")
'''


#Programa para hallar el area y perimetro de una circunferencia.
#Autor: Manuel Blanco
#fecha: 05/Octubre/2020

#importando libreria math
from math import pi

#Encabezado del programa.
print("¡Vamos a hallar el area y el perimetro de una circunferencia! ")

#Peticion de datos.
radio = float(input("Inserta el radio (en metros), luego pulsa la tecla enter: "))

#Calculos
area = pi * radio ** 2
perimetro = (radio *2) * pi

#Impresion de resultados por pantalla.
print(f"El area de la circunferencia es: {round(area, 2)} metros.")
print(f"El perimetro de la circunferencias es: {round(perimetro, 2)} metros.")