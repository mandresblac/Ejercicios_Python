#Trabajo son cadenas de texto.

#Las cadena pueden tratarse como listas.

cadena = "hola como estan ustedes?"


# En positivo
#  H o l a   c o m o    e  s  t  a  n     u  s  t  e  d  e  s  ?
#  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23

#En negativo
#  H  o   l   a        c   o   m   o      e   s   t   a   n      u  s  t  e  d  e  s  ?
#-24 -23 -22 -21 -20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

#Nota: Las cadenas de caracters o Strings (str) son inmutables, es decir no se pueden modificar a diferencia de lasa listas
#que son mutables, es decir si se pueden modificar.

letra = cadena[5]
modificada = cadena.split()

print(letra)
print(cadena[:10])
print(cadena[10:])
print(cadena[:-20])
print(cadena[-8:])
print(cadena[5:15])
print(cadena.capitalize())
print(cadena.lower())
print(cadena.upper())
print(cadena.isupper())
print(cadena.split())
print(modificada[2])

