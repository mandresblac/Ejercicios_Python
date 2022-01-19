# Este es un juego de adivinar los números.

import random

numero_secreto = random.randint(1, 20)
print('Estoy pensando un número entre 1 y 20.')

# Pídale al jugador que adivine 6 veces.
for conjetura in range(1, 7):
    adivina = int(input('Intenta adivinarlo, inserta un número: '))

    if adivina < numero_secreto:
        print()
        print('Número bajo, inserta un número mas alto')
    elif adivina > numero_secreto:
        print()
        print('Número alto, inserta un número mas bajo')
    else:
        break # ¡Esta condición es la suposición correcta!

if adivina == numero_secreto:
    print('¡Buen trabajo! Adivinaste mi número en', str(conjetura), 'intentos!')
else:
    print('No. El número en el que estaba pensando era', str(numero_secreto))