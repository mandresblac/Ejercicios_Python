#Bucle while

#Ejercicio 1
"""
i=0
while i<=3:
    print(i, end=' ')
    i += 1 # i = i + 1
print('Hecho')
"""

#Ejercicio 2
"""
i=0
while i<10:
    print(i, end=' ')
    i += 2 # i = i + 2
print('Hecho')
"""

#Ejercicio 3
"""
i=3
while i < 10:
    i += 2
    print(i, end=' ')
print('Hecho')
"""

#Ejercicio 4
"""
i=1
while i < 100:
    i *= 2
    print(i, end=' ')
"""

#Ejercicio 5
"""
i = int(input('Valor inicial: '))
while i < 10:
    print(i, end=' ')
    i += 1
"""

#Ejercicio 5
"""
i = int(input('Valor inicial: '))
limite = int(input('Limite: '))
incremento = int(input('Incremento: '))

while i <= limite:
    print(i, end=' ')
    i += incremento
"""

#Ejercicio 6
"""
sumatoria=0
i=1
while i <= 1000:
    sumatoria += i
    i += 1
print(sumatoria)
"""

#Ejercicio 7
"""
sumatoria=0
i=1
while i <= 1000:
    i += 1
    sumatoria += i
print(sumatoria)
"""

#Ejercicio 8
"""
nombre=input('Ingresa tu nombre: ')
apellido=input('Ingresa tu apellido: ')
nacionalidad=input('Ingresa tu nacionalidad: ')

print('tu nombre es {0} {1} y eres de nacionalidad {2}'.format(nombre, apellido, nacionalidad))
"""

#Ejercicio 9 - Raiz cuadrada.
"""
from math import sqrt

#x=-1
x = float(input('Introduce un número positivo: '))
while x < 0:
    x = float(input('Introduce un número positivo: '))

print('La raiz cuadrada de {0} es {1}'.format(x, sqrt(x)))
print(f'La raiz cuadrada de {x} es {sqrt(x)}')
"""

#Ejercicio 10
"""
'''Diseña un programa que solicite la lectura de un número entre 0 y 10 (ambos inclusive). Si el usuario teclea un número fuera del rango valido, el programa solicitara nuevamente la introduccion del valor cuantas veces sea necesario.'''

numero=int(input('Introduce un número entre 0 y 10: '))

while numero < 0 or numero > 10:
    numero=int(input('Introduce un número entre 0 y 10: '))

print('{} esta entre 0 y 10'.format(numero))
"""
#Ejercicio 11