"""
print()
print('''Querida Alicia,
el "gato" de Julia
ha sido arrestado por secuestro.
Atentamente,
Manuel''')
"""

'''
saludo = input('Hola, como estas?: ')

if saludo.lower() == 'genial':
    print('Yo tambien me siento genial.')
else:
    print('Espero que el resto de día sea bueno.')
'''

while True:
    edad = input('Ingresa tu edad: ')

    if edad.isdecimal():
        break
    print('Por favor ingresa un número para tu edad.')

while True:
    contraseña = input('Selecciona una nueva contraseña (letras y números): ')
    if contraseña.isalnum():
        break
    print('Las contraseñas solo pueden tener letras y números.')


