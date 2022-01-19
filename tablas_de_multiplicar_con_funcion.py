#Tablas de multiplicar con una funcion que contiene un ciclo for.

def imprimir_tabla(numero, desde, hasta):
    #Definicion de la funcion con un ciclo for.
    for i in range(desde, hasta + 1):
        print(f'{numero} x {i} = {numero * i}')

print()
print(' TABLAS DE MULTIPLICAR '.center(129, '*'))
n1=int(input('Ingrese un número: '))
n2=int(input('Ingrese el número desde el cual quiere que inicie la tabla: '))
n3=int(input('Ingrese el número con el cual quiere que termine la tabla: '))

print()
print('Tabla del {}'.format(n1))

#Llamada de la funcion.
imprimir_tabla(n1, n2, n3)

