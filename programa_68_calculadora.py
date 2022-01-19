#Calculadora

print()
print(' CALCULADORA '.center(125, '*'))

print('BIENVENIDO')
print()

while True:
    opcion=input('''Que quiere hacer? Escoja una opción \n1) Realizar una operación aritmetica (suma, resta, miltiplicacion, division o potencia). \n2) Salir. \n:''')

    print()
    if opcion == '1':
        n1=float(input('Inserte un número: '))
        n2=float(input('Inserte otro número: '))
        print('''\nPara sumar oprima la tecla + \nPara restar oprima la tecla - \nPara multiplicar oprima la tecla x \nPara dividir oprima la tecla / \nPara potencia oprima dos veces la tecla **''')

        operacion=input('\nEscoja que tipo de operacion desea realizar: ')

        if operacion == '+':
            print('{} + {} = {}'.format(n1, n2, n1 + n2))
            print()
        elif operacion == '-':
            print('{} - {} = {}'.format(n1, n2, n1 - n2))
            print()
        elif operacion == 'x':
            print('{} x {} = {}'.format(n1, n2, n1 * n2))
            print()
        elif operacion == '/':
            print('{} / {} = {}'.format(n1, n2, n1 / n2))
            print()
        else:
            operacion == '**'
            print('{} ** {} = {}'.format(n1, n2, n1 ** n2))
            print()
    elif opcion == '2':
        print('Adios, ha sido un placer ayudarte.')
        break
    else:
        print('ERROR, Orden desconocida, vuelve a intentarlo.')
        print()

