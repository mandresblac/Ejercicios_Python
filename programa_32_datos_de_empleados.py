#Programa que muestra los datos de los empleados.

#Listas de datos.
empleados, edad, profesion, ciudad  = ['Andrea Perez', 'Juan Sarmiento', 'Raul Castro', 'Gloria Torres', 'Milena Diaz'], [35, 42, 31, 29, 30], ['abogada', 'ingeniero industrial', 'arquitecto', 'psicologa', 'publicista'], ['Bogota', 'Cali', 'Cartagena', 'Medellín', 'Cartagena']

#Cabecera del programa.
print()
print('\t' * 5, '*' * 24)
print('\t' * 5, '**','LISTA DE EMPLEADOS', '**')
print('\t' * 5, '*' * 24)
print('\t' * 5, '1-', empleados[0], '\n','\t' * 5, '2-', empleados[1], '\n', '\t' * 5, '3-', empleados[2], '\n', '\t' * 5, '4-', empleados[3],'\n','\t' * 5, '5-', empleados[4])
print()

#Recoleccion de datos:
seleccion = int(input('\t\tIngresa el número de la izquierda para conocer los datos del empleado,luego oprime la tecla enter: '))

#Bucle.
while seleccion <= 0 or seleccion > 5:
    print()
    print('\t\tHas introducido un número incorrecto. ¡Vuelve a intentarlo!')
    print('\t' * 5, '1-', empleados[0], '\n','\t' * 5, '2-', empleados[1], '\n', '\t' * 5, '3-', empleados[2], '\n', '\t' * 5, '4-', empleados[3],'\n','\t' * 5, '5-', empleados[4])
    seleccion = int(input('\t\tIngresa el número de la izquierda para conocer los datos del empleado,luego oprime la tecla enter: '))

#Seleccion de alterantivas.
if seleccion == 1:
    print(f'\t\t{empleados[0]} tiene {edad[0]} años, es {profesion[0]} y vive en la ciudad de {ciudad[0]}.')
elif seleccion == 2:
    print(f'\t\t{empleados[1]} tiene {edad[1]} años, es {profesion[1]} y vive en la ciudad de {ciudad[1]}.')
elif seleccion == 3:
    print(f'\t\t{empleados[2]} tiene {edad[2]} años, es {profesion[2]} y vive en la ciudad de {ciudad[2]}.')
elif seleccion == 4:
    print(f'\t\t{empleados[3]} tiene {edad[3]} años, es {profesion[3]} y vive en la ciudad de {ciudad[3]}.')
else:
    seleccion == 5
    print(f'\t\t{empleados[4]} tiene {edad[4]} años, es {profesion[4]} y vive en la ciudad de {ciudad[4]}.')

print()
print('\t' * 5, '¡Fin del programa! ¡ADIOS!')