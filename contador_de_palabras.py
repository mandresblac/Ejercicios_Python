#Contador de palabras

print()
print('CONTADOR DE LETRAS')

cadena=input('Ingrese una o varias palabras: ')
print('\"{0}\" tiene {1} caracteres'.format(cadena, len(cadena)))

"""
#El siguiente programa ejecuta una función que para cada caracter en un string, imprime su valor en la tabla ascii.
def imprimir_numero_ascii(s):
    for i in s:
        print(ord(i), end=' ')

s = input('Ingrese una palabra: ')
print(f'La palabra \"{s}\" equivale a los siguientes valores en la tabla ASCII:', end=' ')
imprimir_numero_ascii(s)
print()
"""

"""
s = input('Ingresa una palabra: ')
for i in s:
    print(i, end=' ')
"""