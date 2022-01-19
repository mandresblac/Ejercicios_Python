'''
print('Tabla del 5')

def dibujar_tabla_del_5():
    for i in range(11):
        print('5 *', i, '=', i * 5)
dibujar_tabla_del_5()
'''

nombre = input('Ingrese su nombre: ')
apellido = input('Íngrese su apellido: ')
edad = int(input('Ingrese su edad: '))
print('Hola ' + nombre + ' ' + apellido + ',' + ' tu tienes ' + str(edad) + ' años.')
print(f'Hola {nombre} {apellido}, tu tienes {edad} años.')