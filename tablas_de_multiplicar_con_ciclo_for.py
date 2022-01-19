#Tabla de multiplicar

print()
print(' TABLAS DE MULTIPLICAR '.center(129, '*'))
print()

while True:
    try:
        numero=int(input('Ingrese un número: '))
        desde=int(input('Ingrese el número desde el cual quiere que inicie la tabla: '))
        hasta=int(input('Ingrese el número con cual quiere que termine la tabla: '))
        break
    except ValueError:
        print("No se pueden introducir letras. ¡Intentalo de nuevo con un número!")
    except Exception:
        print(("No se permiten edades negativas"))


print()
print('Tabla del {}'.format(numero))
for i in range(desde, hasta + 1):
    print(f'{numero} x {i} = {numero * i}')

