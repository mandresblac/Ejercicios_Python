# Programa para ordenar 3 números de mayor a menor utilizando condicionales

def mayor(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(n1)
    elif n2 > n1 and n2 > n3:
        print(n2)
    else:
        n3 > n1 and n3 > n2
        print(n3)
    return

def menor(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        print(n1)
    elif n2 < n1 and n2 < n3:
        print(n2)
    else:
        n3 < n1 and n3 < n2
        print(n3)
    return

def intermedio(n1, n2, n3):
    a = max(n1, n2, n3)
    b = min(n1, n2, n3)
    c = (n1 + n2 + n3) - a - b
    print(c)

while(True):
    try:
        print()
        print('PROGRAMA PARA ORDENAR 3 NÚMEROS DE MENOR A MAYOR'.center(100, '*'))
        print()
        num1 = int(input('Digite el primer número, luego oprima la tecla enter: '))
        num2 = int(input('Digite el segundo número, luego oprima la tecla enter: '))
        num3 = int(input('Digite el tercer número, luego oprima la tecla enter: '))
        
        print()
        print('El número mayor es:', end=' ')
        mayor(num1, num2, num3)

        print('El número intermedio es:', end=' ')
        intermedio(num1, num2, num3)

        print('El número menor es:', end=' ')
        menor(num1, num2, num3)
    except:
        print('Ha ocurrido un error, introduce bien el número.')
    else:
        print()
        print('Fin del programa', end=' ')
        break  # Importante romper la iteración si todo ha salido bien.
    finally:
        print('¡ADIOS!')