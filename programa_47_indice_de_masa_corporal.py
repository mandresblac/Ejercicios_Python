# Programa para calcular el indice de masa corporal (IMC).
print()
print(' PROGRAMA PARA CALCULAR EL INDICE DE MASA CORPORAL (IMC) '.center(129, "*"))
print()

# Definicion de funcion.
def imc(estatura, peso):
    '''
    Calcula el indice de masa corporal.
    '''
    return peso / estatura ** 2

# Recoleccion de datos.
peso =float(input('Escriba su peso (Kg), luego oprima la tecla enter: '))
estatura =float(input('Escriba su estatura (m), luego oprima la tecla enter: '))

#Procesamiento de datos,
#Llamada de la funcion imc dentro de la variable indice.
indice = imc(estatura, peso)

#Salida de resultados.
if indice < 18.5:
    print('Su IMC es: {}'.format(round(indice, 2)))
    print('Bajo de peso.')
elif indice >= 18.5 and indice <= 24.9:
    print('Su IMC es: {}'.format(round(indice, 2)))
    print('Peso normal.')
elif indice >= 25 and indice <= 29.9:
    print(f'Su IMC es: {round(indice, 2)}')
    print('Sobrepeso')
elif indice >= 30 and indice <= 34.9:
    print(f'Su IMC es: {round(indice, 2)}')
    print('Obesidad grado I')
elif indice >= 35 and indice <= 39.9:
    print(f'Su IMC es: {round(indice, 2)}')
    print('Obesidad grado II')
elif indice >= 40 and indice <= 49.9:
    print(f'Su IMC es: {round(indice, 2)}')
    print('Obesidad grado III')
else:
    indice > 50
    print(f'Su IMC es: {round(indice, 2)}')
    print('Obesidad grado IV')



