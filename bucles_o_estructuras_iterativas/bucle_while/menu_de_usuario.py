#Menu de usuario
print(" BIENVENIDO ".center(135, '-'))

while (True):
    opcion=input('''\nQue quieres hacer? Ingresa una opción:
            \n1- saludar \n2- Sumar dos números \n3- Salir \n:''')
    if opcion == '1':
        print("\nHola, como te encuentras el dia de hoy")
        print('-'* 135)
    elif opcion == '2':
        n1=float(input("Ingresa el primer número: "))
        n2=float(input("Ingresa el segundo número: "))
        print("\nEl reultado de sumar {} + {} es: {}".format(n1, n2, n1 + n2))
        print('-'* 135)
    elif opcion == '3':
        print("\nDios me lo bendiga, licenciado.")
        print('-'* 135)
        break
    else:
        print("\nNo hay manera socio, intenta de nuevo.")
        print('-'* 135)

