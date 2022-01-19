
print('MEDIA DE NÚMEROS')

contador = 0
suma = 0
numero = 1

while numero != 0:
    numero=float(input('Igrese un número entero (o 0 para terminar): '))
    if numero != 0:
        suma += numero
        contador += 1

if contador == 0:
    print('No digito ningun número.')
else:
    promedio = suma / contador
    print('El promedio de los {} números ingresados es igual a {}'.format(contador, promedio))








