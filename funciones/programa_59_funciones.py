#Funciones

#Ejercicio 1
"""
def suma(numero1, numero2):
    print('El resultado es: {}'.format(numero1 + numero2))
    print(f'El resultado es: {numero1 + numero2}')

n1=int(input('Ingresa el primer número: '))
n2=int(input('Ingresa el segundo número: '))

suma(n1, n2)
"""

#Ejercicio 2

def suma(n1, n2):
    resultado = n1 + n2
    return resultado

n1=int(input('Ingresa el primer número: '))
n2=int(input('Ingresa el segundo número: '))

print('{} + {} = {}'.format(n1, n2, suma(n1, n2)))

