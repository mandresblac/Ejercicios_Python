'''
nombresGatos = []

while True:
    print('Ingrese el nombre del gato' + str(len(nombresGatos) + 1) + '(O ingrese nada para detener):')
    nombre =input()
    if nombre == "":
        break
    nombresGatos = nombresGatos + [nombre] #Lista concatenacion.

print('Los nombres de los gatos son: ')
for nombre in nombresGatos:
    print(' ' + nombresGatos)
'''

'''
for i in [0, 1, 2, 3]:
    print(i)
'''


suministros = ['bolígrafos', 'grapadoras', 'lanzallamas', 'carpetas']
for i in range(len (suministros)):
    print ('Indice ' + str(i) + ' en suministros es: ' + suministros [i])