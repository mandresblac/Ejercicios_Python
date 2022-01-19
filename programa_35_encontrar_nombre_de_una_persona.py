'''
#Progama encontrar el nombre de un alumno dentro de una lista dada.

alumnos = ['Maria', 'Carlos', 'Diego', 'Luis', 'Esteban', 'Carolina', 'Pilar']

nombre = input('Ingresa el nombre del alumno: ')

while nombre not in alumnos:
    print('No hay ningun alumno llamado: ' + nombre)
    nombre = input('Ingresa el nombre del alumno: ')

if nombre in alumnos:
    print(nombre + ' si es mi alumno:')

print('Fin del programa.')
'''


suministros = ['bolígrafos', 'engrapadoras', 'lanzallamas', 'carpetas']

for index, articulo in enumerate(suministros):
    print('indice ' + str(index) + ' en suminitros es: ' + articulo)
