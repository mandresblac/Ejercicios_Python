#BUCLES FOR NO ANIDADOS

#Programa 1
#Programa que pide la anchura de una línea y la dibuja con caracteres asterisco (*):
'''
anchura = int(input('Anchura de la línea: '))

for i in range(anchura):
    print('*', end='')
'''


#Programa 2
#Programa que pide la anchura de una línea y la dibuja con caracteres asterisco (*) y guion (-):
'''
anchura = int(input('Anchura de la línea: '))

print('*', end='')
for i in range(anchura - 2):
    print('-', end='')
print('* ')
'''


#Programa 3
#Programa que pide la altura de una figura y la dibuja con caracteres asterisco (*):
'''
altura = int(input('Altura de la figura: '))

for i in range(altura):
    print('*')
'''


#Programa 4
#Programa que pide la altura de una figura y la dibuja con caracteres asterisco (*) y tubería (|):
'''
altura =int(input('Altura de la figura: '))

print('* ')
for i in range(altura - 2):
    print('|')
print('* ')
'''

#BUCLES FOR ANIDADO

#Programa 5
#programa que pide la anchura y altura de un rectángulo y lo dibuja con caracteres asterisco (*):
'''
anchura = int(input('Anchura del rectangulo: '))
altura = int(input('Altura del rectangulo: '))

for i in range(altura):
    for j in range(anchura):
        print('* ', end='')
    print()
'''


#Programa 6
#Programa que pide la anchura y altura de un rectángulo y lo dibuja con caracteres asterisco (*) y guion (-):
'''
anchura = int(input('Anchura del rectangulo: '))
altura = int(input('Altura del rectangulo: '))

for i in range(anchura):
    print('* ', end='')
print()

for i in range(altura - 2):
    print('* ', end='')
    for j in range(anchura - 2):
        print('  ', end='')
    print('*')

for i in range(anchura):
    print('* ', end='')
print()
'''


#Programa 7
#Programa que pide la anchura y altura de un rectángulo y la cantidad de rectángulos a dibujar uno debajo del otro y los dibuja con caracteres asterico (*) y espacios:
'''
anchura = int(input('Anchura del rectangulo: '))
altura = int(input('Altura del rectangulo: '))
numero = int(input('Numero de rectangulos en vertical: '))

for k in range(anchura):
    print('* ', end='')
print()

for i in range(numero):
    for j in range(altura -2):
        print('* ', end='')
        for k in range(anchura - 2):
            print('  ', end='')
        print('*')

    for k in range(anchura):
        print('* ', end='')
    print()
'''


#Programa 8
#Programa que pide la anchura y altura de un rectángulo y la cantidad de rectángulos a dibujar uno al lado del otro y los dibuja con caracteres asterisco (*) y espacios:
'''
anchura = int(input('Anchura del rectangulo: '))
altura = int(input('Altura del rectangulo: '))
numero = int(input('Numero de rectangulos en horizontal: '))

for j in range(anchura * numero - numero + 1):
    print('* ', end='')
print()

for i in range(altura - 2):
    for k in range(numero):
        print('* ', end='')
        for j in range(anchura - 2):
            print('  ', end='')
    print('*')

for j in range(anchura * numero - numero + 1):
    print('* ', end='')
print()
'''


#Programa 9
#Programa que pide la anchura y altura de un rectángulo y la cantidad de rectángulos a dibujar uno al lado del otro y lo dibuja con caracteres asterisco (*) y espacios:
'''
anchura = int(input('Anchura del rectangulo: '))
altura = int(input('Altura del rectangulo: '))
horizontal = int(input('Numero de rectangulos en horizontal: '))
vertical = int(input('Numero de rectangulos en vertical: '))

for j in range(anchura * horizontal - horizontal + 1):
    print('* ', end='')
print()

for l in range(vertical):
    for i in range(altura - 2):
        for k in range(horizontal):
            print('* ', end='')
            for j in range(anchura - 2):
                print('  ', end='')
        print('* ')
    
    for j in range(anchura * horizontal - horizontal + 1):
        print('* ', end='')
    print()
'''


#Programa 10
#Programa que pide la altura, la anchura y el grosor de una letra L y la dibuja con caracteres asterisco (*).
'''
print('Letra L')
altura = int(input('Altura de la letra L: '))
anchura = int(input('Anchura de la letra L: '))
grosor = int(input('Grosor de la letra L: '))

if altura <= 0 or anchura <= 0 or grosor <= 0:
    print('Los tres valores deben ser positivos.')
elif altura <= grosor:
    print('La altura debe ser mayor que el grosor.')
elif anchura <= grosor:
    print('La anchura debe ser mayor que el grosor.')
else:
    for i in range(altura - grosor):
        for j in range(grosor):
            print('* ', end='')
        print()
    
    for i in range(grosor):
        for j in range(anchura):
            print('* ', end='')
        print()
'''


#Programa 11
#Programa que pide la altura, la anchura y el grosor de una letra C y la dibuja con caracteres asterisco (*).
'''
print("Letra C")
altura = int(input("Altura de la letra C: "))
anchura = int(input("Anchura de la letra C: "))
grosor = int(input("Grosor de la letra C: "))

if altura <= 0 or anchura <= 0 or grosor <= 0:
    print("Los tres valores deben ser positivos.")
elif altura <= 2 * grosor:
    print("La altura debe ser mayor que el doble del grosor.")
elif anchura <= grosor:
    print("La anchura debe ser mayor que el grosor.")
else:
    for i in range(grosor):
        for j in range(anchura):
            print("* ", end="")
        print()

    for i in range(altura - 2 * grosor):
        for j in range(grosor):
            print("* ", end="")
        print()

    for i in range(grosor):
        for j in range(anchura):
            print("* ", end="")
        print()
'''


#Programa 12
#Programa que pida la altura, la anchura y el grosor de una letra U y la dibuje con caracteres asterisco (*).
'''
print("Letra U")
altura = int(input("Altura de la letra U: "))
anchura = int(input("Anchura de la letra U: "))
grosor = int(input("Grosor de la letra U: "))

if altura <= 0 or anchura <= 0 or grosor <= 0:
    print("Los tres valores deben ser positivos.")
elif altura <= grosor:
    print("La altura debe ser mayor que el grosor.")
elif anchura <= 2 * grosor:
    print("La anchura debe ser mayor que el doble del grosor.")
else:
    for i in range(altura - grosor):
        for j in range(grosor):
             print("* ", end="")
        for j in range(anchura - 2 * grosor):
            print("  ", end="")
        for j in range(grosor):
            print("* ", end="")
        print()

    for i in range(grosor):
        for j in range(anchura):
            print("* ", end="")
        print()
'''
