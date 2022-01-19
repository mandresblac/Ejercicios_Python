#Concatenar una n cantidad de cadenas de caracteres con join
'''
lenguajes = ['Python', 'C#', 'Java', 'JavaScript', 'Kotlin', 'Go', 'PHP']

cadena = ' - '.join(lenguajes)

print(cadena)
'''


#Comprobar que todos los elementos de una cadena son mayores respecto a un número
'''
numeros = [7, 3, 2, 5, 11, 20]

print(all(x > 1 for x in numeros))
print(all(x <= 10 for x in numeros))
'''


#Contar la cantidad de veces que se repite un caracter dentro de una cadena de caracteres.
'''
cadena = """Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código.
          Se trata de un lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación
          imperativa y, en menor medida, programación funcional."""

cantidad_a= cadena.count('a')
cantidad_e= cadena.count('e')
cantidad_n= cadena.count('n')
cantidad_r= cadena.count('r')
cantidad_f= cadena.count('f')
cantidad_ñ= cadena.count('ñ')
cantidad_y= cadena.count('y')

print(f'La cantidad del caracter "a" es igual a: {cantidad_a} ')
print(f'La cantidad del caracter "e" es igual a: {cantidad_e} ')
print(f'La cantidad del caracter "n" es igual a: {cantidad_n} ')
print(f'La cantidad del caracter "r" es igual a: {cantidad_r} ')
print(f'La cantidad del caracter "f" es igual a: {cantidad_f} ')
print(f'La cantidad del caracter "ñ" es igual a: {cantidad_ñ} ')
print(f'La cantidad del caracter "y" es igual a: {cantidad_y} ')
'''

#Obtener el valor númerico de un caracter ASCII

perfil_twitter = '@Python'

for i in perfil_twitter:
    print('%s:%i' % (i, ord(i)))


