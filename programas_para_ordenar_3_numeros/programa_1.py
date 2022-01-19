# Programa para ordenar 3 números de menor a mayor sin usar condicionales ni ciclos.

print()
print('*' * 49)
print('PROGRAMA PARA ORDENAR 3 NÚMEROS DE MENOR A MAYOR')
print('*' * 49)
print()
x = int(input('Escriba el primer número: '))
y = int(input('Escriba el segundo número: '))
z = int(input('Escriba el tercer número: '))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c

# primer número = 1
# segundo número = 2
# tercer número = 3
# a = 1
# c = 3
# b = (1 + 2 + 3) - 1 - 3
# b = 6 - 1 - 3 = 2

print()
print('*' * 28)
print(f'El número menor es: {str(a)}')
print(f'El número mayor es: {str(c)}')
print(f'El número intermedio es: {str(b)}')
print('*' * 28)

