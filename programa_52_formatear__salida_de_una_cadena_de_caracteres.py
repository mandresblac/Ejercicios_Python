#Ejemplos de como formatear la salida de una cadena de caracteres en Python.
#Ejemplo 1

destino1 = 'playa'
destino2 = 'parque'
cantidad = 3

print('Fui a la {} y al {} {} veces esta semana'.format(destino1, destino2, cantidad
    ))


#Esplicacion:
"""
La primera variable que creamos es destino1. Establecemos esta variable igual a "playa"
La segunda variable que creamos es destino2. Establecemos esta variable igual a "parque"
La tercera variable que creamos es la cantidad. Establecemos esta variable igual a 3.

Luego creamos una declaración impresa.

Cada vez que vea {} en la declaración de impresión, esto representa un marcador de posición.
Lo que hace un marcador de posición es mantener un lugar para una variable. Cuando hacemos la sustitución, la variable
aparecerá en el lugar de {}.

Verá esto 3 veces en la declaración de impresión, lo que significa que se reservan 3 lugares para las variables.

Una vez que hayamos terminado con la declaración de impresión que termina con comillas (ya sea simple o doble), colocamos
.format (destino1, destino2, cantidad), que representa las 3 variables en el orden que queremos que se sustituyan por los
marcadores de posición.

Al final, esto nos da la declaración de salida: "Fui a la playa y estacioné 3 veces esta semana".
"""

#Ejemplo 2

animal1 = "elefante"
animal2 = "leon"
animal3 = "jirafa"
num = [1, 2, 3]

print('Fui al zoologico ayer y vi {} {}, {} {}es y {} {}s'.format((num[0]), animal1, (num[1]), animal2, (num[2]), animal3))


#Ejemplo 3

x = 2
y = 3
suma = x + y

print('La suma de ' + str(x) + ' y ' + str(y) + ' es igual a: ' + str(suma)) #Concatenacion de cadena de caracteres.
print('La suma de ',  str(x), 'y', str(y), 'es igual a: ', str(suma)) #Cncatenacion con comas.
print('La suma de {} y {} es igual a: {}'.format(x, y, suma)) #Formateo.
print(f'La suma de {x} y {y} es igual a: {suma}') #f
print('La suma de %d y %d es igual a: %d' %(x, y, suma)) #Placeholder.


