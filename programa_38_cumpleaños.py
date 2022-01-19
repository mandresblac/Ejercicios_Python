#Programa para saber la fecha de cumpleaños de la familia.

#Diccionario con los datos.
cumpleaños = {'Yolanda':'15 de Junio', 'Julio Eduardo':'17 de Julio', 'Simon David':'16 de Junio', 'David Eduardo':'18 de Enero', 'Maira Alejandra':'1 de Diciembre', 'Manuel Andres':'10 de Abril'}

print()
print('PROGRAMA PARA CONOCER LA FECHA DE CUMPLEAÑOS DE LA FAMILIA')
print()
print('''Los miembros de la familia son:
- Yolanda
- Julio Eduardo
- Simon David
- David Eduardo
- Maira Alejandra
- Manuel Andres''' )


while True:
    print()
    nombre = input('Ingrese el nombre de un miembro de la familia (En blanco para salir): ')
    if nombre == '':
        break
    elif nombre in cumpleaños:
        print(f'El {cumpleaños[nombre]} es el cumpleaños de {nombre}.')
    else:
        print('No tengo informacion de cumpleaños para ' + nombre)
        cumpleaños2 = input('¿Cual es su cumpleaños?')
        cumpleaños[nombre] == cumpleaños2
        print('Base de datos de cumpleaños actualizada.')
