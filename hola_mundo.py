#Este programa dice hola y me pregunta por mi nombre

print('¡Hola Mundo!')
#print('¿Como te llamas?: ') #Pregunta por su nombre

myNombre = input('¿Como te llamas?: ')
print('Es un gusto conocerte: ' + myNombre)

print()
print('La longitud de tu nombre es: ')
print(len(myNombre) , 'carateres.')

print()
#print('¿Cual es tu edad?: ') #Pregunta por su edad.
miEdad = int(input('¿Cual es tu edad?: '))
#print('Tu tendras ' + str(int(miEdad) + 1) + ' en un año.')
print('Tu tendras ' + str(miEdad + 1) + ' en un año.')