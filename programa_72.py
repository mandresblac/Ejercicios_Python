
n1 = float(input('Introduce un número: '))
n2 = float(input('Introduce otro número: '))

print()
print('Que quieres hacer?:')
print('''1- Sumar los dos números. \n2- Restar los dos números. \n3- Multiplicar los dos números. ''')
opcion= input('Introduce una opción: ')

if opcion == '1':
    print()
    print('La resultado de sumar {} + {} es {}'.format(n1, n2, n1 + n2))
elif opcion == '2':
    print()
    print('La resultado de restar {} - {} es {}'.format(n1, n2, n1 - n2))
elif opcion == '3':
    print()
    print('La resultado de multiplicar {} * {} es {}'.format(n1, n2, n1 * n2))
else:
    print()
    print('La opción es incorrecta.')


