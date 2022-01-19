# Programa para ordenar 3 números de mayor a menor sin usar condicionales ni ciclos.

while(True):
    try:
        print()
        print('PROGRAMA PARA ORDENAR 3 NÚMEROS DE MENOR A MAYOR'.center(100, '-'))
        print()
        num1 = int(input('Digite el primer número, luego oprima la tecla enter: '))
        num2 = int(input('Digite el segundo número, luego oprima la tecla enter: '))
        num3 = int(input('Digite el tercer número, luego oprima la tecla enter: '))
        
        a = max(num1, num2, num3)
        b = min(num1, num2, num3)
        c = (num1 + num2 + num3) - a - b
        
        print()
        print('El número mayor es: {}'.format(str(a)))
        print(f'El número menor es: {str(b)}')
        print('El número intermedio es: {}'.format(str(c)))
    except:
        print()
        print('Ha ocurrido un error, introduce bien el número.')
    else:
        print()
        print('Todo ha funcionado correctamente.')
        break  # Importante romper la iteración si todo ha salido bien.
    finally:
        print('Fin de la iteración.')

