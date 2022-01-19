#Programa para hallar el promedio de notas de los alumnos.

print()
print('\t' * 4, 'PROGRAMA PARA HALLAR EL PROMEDIO DE NOTAS DE ALUMNOS')
print()

#Recoleccion de 
print('\t' * 2, 'Ingrese 3 notas de 0 a 5.')
print()
nota1 = float(input('\t\t Primera nota: '))
nota2 = float(input('\t\t Segunda nota: '))
nota3 = float(input('\t\t Tercer nota: '))

while nota1 < 0 or nota1 > 5 or nota2 <= 0 or nota2 > 5 or nota3 <= 0 or nota3 > 5:
    print('\t' * 2, 'Has introducido un número incorrecto, vuelve a intentarlo')
    nota1 = float(input('\t\t Primera nota: '))
    nota2 = float(input('\t\t Segunda nota: '))
    nota3 = float(input('\t\t Tercer nota: '))

#Procesamiento de datos
promedio = ((nota1 + nota2 + nota3) / 3)

#Salida de datos
if promedio < 3.0:
    print()
    print('\t' * 2, 'la nota final es', round(promedio, 2))
    print('\t' * 2, '😰😰 ¡REPROBO! 😰😰')
else:
    promedio >= 3.0 or promedio < 5
    print()
    print('\t' * 2, 'la nota final es', round(promedio, 2))
    print('\t' * 2, '😀😀 ¡APROBO! 😀😀')

print()
print('\t' * 2, 'Fin del programa, ¡ADIOS!')
