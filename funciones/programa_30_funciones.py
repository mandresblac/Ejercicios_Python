'''
#Este es el programa 1
def hola():
    print('¡Hola!')
    print('¡Hola!!!!')
    print('¡Hola a todos')

hola()
hola()
hola()
'''

'''
#Este es el programa 2
def hola(nombre):
    print('Hola ' + nombre)

hola('Alicia')
hola('Pancracio')
'''

'''
#Este es el programa 3
import random

def respuesta(numeroRespuesta):
    if numeroRespuesta == 1:
        return 'Es cierto'
    elif numeroRespuesta == 2:
        return 'Es decididamente así'
    elif numeroRespuesta == 3:
        return 'si'
    elif numeroRespuesta == 4:
        return 'Respuesta confusa, intenta otra vez'
    elif numeroRespuesta == 5:
        return 'Pregunta de nuevo más tarde'
    elif numeroRespuesta == 6:
        return 'Concéntrate y pregunta otra vez'
    elif numeroRespuesta == 7:
        return 'Mi respuesta es no'
    elif numeroRespuesta == 8:
        return 'Outlook no es tan bueno'
    elif numeroRespuesta == 9:
        return 'Muy dudoso'

print(respuesta(random.randint(1, 9)))
'''
'''
print('Hola', end=' ')
print('mundo', end=' ')
print('como', end=' ')
print('vas')
'''


print('Gatos', ' Perros', ' Ratones', sep=',')

