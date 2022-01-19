# METODOS DE CADENA DE CARACTERES O STRING str().

cadena = 'yo soy una cadena de texto'
numeros = '1234'

# 1-METOODS DE ANALISIS:

'''El método count() retorna el número de veces que se repite un conjunto de caracteres especificado.'''
print(cadena.count('a'))

'''Los métodos find() e index() retornan la ubicación (comenzando desde el cero) en la que se encuentra el argumento indicado.
Difieren en que  la última lanza ValueError cuando el argumento no es encontrado, mientras que la primera retorna -1. En ambos métodos la búsqueda ocurre de izquierda a derecha.'''
print(cadena.find('una'))
print(cadena.index('cadena'))

'''los metodos startswith() y endswith() indican si la cadena en cuestión comienza o termina con el conjunto de caracteres pasados como argumento, y retornan True o False en función de ello.'''
print(cadena.startswith('yo'))
print(cadena.startswith('una'))
print(cadena.endswith('texto'))
print(cadena.startswith('de'))

'''Los métodos isdigit(), isnumeric() e isdecimal() determinan si todos los caracteres de la cadena son dígitos, números o números decimales.'''
print(cadena.isdigit())
print(numeros.isnumeric())
print(numeros.isdecimal())


# 2-METODOS DE TRANSFORMACION:

'''Recuérde que las cadenas son inmutables; por ende, todos los métodos a continuación no actúan sobre el objeto original sino que retornan uno nuevo.'''

#capitalize() retorna la cadena con su primera letra en mayúscula.
print(cadena.capitalize())

'''lower() y upper() retornan una copia de la cadena con todas sus letras en minúsculas o mayúsculas según corresponda.'''
print(cadena.upper())
print(cadena.lower())

'''swapcase(), por su parte, cambia las mayúsculas por minúsculas y viceversa.'''
print(cadena.swapcase())

'''encode() codifica la cadena con el mapa de caracteres especificado y retorna una instancia del tipo bytes.'''
print(cadena.encode('utf-8'))

'''Los métodos center(), ljust() y rjust() alinean una cadena en el centro, la izquierda o la derecha respectivamente. Toman un argumento, la cantidad de caracteres respecto de la cual se producirá la alineación.
Estos métodos son especialmente útiles al imprimir en forma de tabla para que ésta se mantenga alineada. Un segundo argumento indica con qué caracter se deben llenar los espacios vacíos (por defecto un espacio en blanco).
'''
print(cadena.center(50))
print(cadena.ljust(50))
print(cadena.rjust(50))
print(cadena.center(50, "-"))
print(cadena.ljust(50, '-'))
print(cadena.rjust(50, '-'))

'''Las funciones strip(), lstrip() y rstrip() remueven los espacios en blanco que preceden y/o suceden a la cadena.'''
print(cadena.strip())
print(cadena.lstrip()) #Remueve los de la izquierda.
print(cadena.rstrip()) #Remueve los de la derecha.

'''El método replace() ─ampliamente utilizado─ reemplaza una cadena por otra. El primer elemento es el elemento a remplazar dentro de la cadena, despues de la coma se escribe el elemento que va a remplazar al primer elemento.'''
print(cadena.replace('una', '5'))


# 3-METODOS DE SEPARACIÓN Y UNIÓN:

'''El método de división de una cadena según un caracter separador más empleado es split(), cuyo separador por defecto son espacios en blanco y saltos de línea.'''
print(cadena.split(' '))
print(cadena.splitlines())

'''Un segundo argumento en split() indica cuál es el máximo de divisiones que puede tener lugar (-1 por defecto para representar una cantidad ilimitada).'''
print(cadena.split(' ', 2))

'''Un segundo método de separación es partition(), que retorna una tupla de tres elementos: el bloque de caracteres anterior a la primera ocurrencia del separador, el separador mismo, y el bloque posterior.'''
print(cadena.partition(' '))

'''rpartition() opera de forma similar, pero realizando la búsqueda de derecha a izquierda.'''
print(cadena.rpartition(' '))

'''El método join() ─sumamente útil─, que debe ser llamado desde una cadena que actúa como separador para unir dentro de una misma cadena resultante los elementos de una lista.'''
print('--'.join(['Hola', 'mundo']))