#Programa que relaciona un número con una letra del abecedario.

print()
print(' PROGRAMA QUE RELACIONA UN NÚMERO CON UNA LETRA DEL ABECEDARIO '.center(129, '*'))
print()

#Diccionario con las letras del abecedario.
abecedario= {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'ñ', 16:'o', 17:'p', 18:'q', 19:'r', 20:'s', 21:'t', 22:'u', 23:'v', 24:'w', 25:'x', 26:'y', 27:'z'}

#Captura de datos
numero = int(input('Las letras del abecedario son 27, escoge una letra insertando un número entre 1 y 27: '))

#Bucle while no permite que el usuario se salga del rango de números establecido.
while numero < 1 or numero > 27:
    print('¡Número fuera de rango!')
    numero= int(input('Inserta un número del 1 al 27: '))

#Bucle for recorre todo el diccionario abecedario.
for i in abecedario.get(numero): #.get devuelve el valor de la clave.
    print('El número {} corresponde a la letra "{}".'.format(numero, i))