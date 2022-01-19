#Programa para calculo de salarios

basico = int(input('Ingrese su sueldo basico: '))
dias = int(input('Ingrese los dias laborados en el mes:'))
hed = int(input('Ingrese horas extras diurnas: '))
hen = int(input('Ingrese horas extras nocturnas: '))

transporte = 3428 * dias
extra_diurna = 4580 * hed
extra_nocturna = 6400 * hen

total1 = basico + transporte + extra_diurna + extra_nocturna
total2 = basico + extra_diurna + extra_nocturna

if basico <= 877803 * 2:
    print(f'Total devengado: {total1}')
else:
    print(f'Total devengado: {total2}')
