"""
#Bucle for

for i in range(5, 50, 3):
    print(f'Valor de la variable {i}')
    #print('Valor de la variable {}'.format(i))
"""

#Bucle while
#Ejercicio 1

"""
edad = int(input('Introduce tu edad: '))

while edad < 5 or edad >= 100:
    print('Has introducido una edad incorrecta, vuelve a intentarlo.')
    edad = int(input('Introduce tu edad: '))

print('Gracias por colaborar. Puedes pasar.')
print('Edad del aspirante: {} años.'.format(edad))
"""

#Bucle while
#Ejercicio 1

"""
import math

print('Programa de calculo de raiz cuadrada.')
numero = int(input('Introduce un número por favor: '))

intentos = 0

while numero < 0 :
    print('No se puede hallar la raiz de un número negativo.')
    if intentos == 2:
        print('Has consumido demasiados intentos. El programa ha finalizado.')
        break #Sale del bucle while y continua ejecucion del programa.

    numero = int(input('Introduce un número por favor: '))
    if numero < 0:
        intentos += 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print('La raiz cuadrada de {} es: {}'.format(numero, solucion))
"""

#Bucle while
#Ejercicio 2

"""
num1 = int(input('Introduce un número: '))
num2 = int(input('Introduce un nímero mayor que {}: '.format(num1)))

while num2 > num1:
    num1 = num2
    num2 = int(input('Introduce un número mayor que {}: '.format(num1)))

print()
print('{} no es mayor que {}'.format(num2, num1))
"""

#Bucle while
#Ejercicio 3

numero = int(input('Introduce un número: '))
suma = 0

while numero > 0:
    suma += numero
    numero = int(input('Introduce un número: '))

print(f'La suma de los números introducidos es {str(suma)}')