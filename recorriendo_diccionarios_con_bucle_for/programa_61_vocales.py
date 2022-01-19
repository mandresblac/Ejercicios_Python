#Programa que relaciona un número con una vocal.

print()
print(' PROGRAMA QUE RELACIONA UN NÚMERO CON UNA VOCAL '.center(129, '*'))
print()

#Lista de vocales.
vocales = {1:'a', 2:'e', 3:'i', 4:'o', 5:'u'}

#captura de datos.
while True:
    try:
        numero= int(input('Las vocales son 5, escoge una vocal insertando un número entre 1 y 5: '))
        break
    except ValueError:
        print("Los valores introducidos no son correctos. ¡Intentalo de nuevo!")

#Bucle while no permite que el usuario se salga del rango de números establecido.
while numero < 1 or numero > 5:
    print('{} es un número fuera de rango!'.format(numero))
    numero= int(input('Inserta un número del 1 al 5: '))

#Bucle for recorre toda la lista vocales.
for i in vocales.get(numero):
    print('El número {} corresponde a la vocal "{}".'.format(numero, i))
