import random, sys

print('JUEGO DE PIEDRA, PAPEL Y TIJERA')

# Estas variables mantienen un registro del número de victorias, derrotas y empates.

victorias = 0
derrotas = 0
empates = 0

while True: #EL bucle principal del juego
    print('%s Victorias \n%s Derrotas \n%s Empates'% (victorias, derrotas, empates))
    print()
    while True: # El bucle de entrada del jugador.
        jugada = input('Escribe una letra, (r)roca (p)papel (t)tijera o (s)salir, luego oprime la tecla enter: ')
        if jugada == 's':
            sys.exit() # Salir del programa.
        else:
            jugada == 'r' or jugada == 'p' or jugada == 't'
            break # Salir del bucle de entrada del reproductor.
        print('Escriba r, p, t o s ')

    # Mostrar lo que eligió el jugador:
    if jugada == 'r':
        print('roca Vs...')
    elif jugada =='p':
        print('papel Vs...')
    else:
        jugada == 't'
        print('tijeras Vs...')

    # Muestra lo que eligió la computadora:
    numeroAleatorio = random.randint(1, 3)
    if numeroAleatorio == 1:
        computerMove = 'r'
        print('roca\n')
    elif numeroAleatorio == 2:
        computerMove = 'p'
        print('papel\n')
    else:
        numeroAleatorio == 3
        computerMove = 't'
        print('tijeras\n')

    # Muestra y registra las victorias / derrotas / empates:
    if jugada == computerMove:
        print ('¡Es un empate!')
        empates += 1
    elif jugada == 'r' and computerMove == 't':
        print ('¡Tu ganas!')
        victorias += 1
    elif jugada == 'p' and computerMove == 'r':
        print ('¡Tu ganas!')
        victorias += 1
    elif jugada == 't' and computerMove == 'p':
        print ('¡Tu ganas!')
        victorias += 1
    elif jugada == 'r' and computerMove == 'p':
        print ('¡Tu pierdes!')
        derrotas += 1
    elif jugada == 'p' and computerMove == 't':
        print ('¡Tu pierdes!')
        derrotas += 1
    else:
        jugada == 't' and computerMove == 'r'
        print ('¡Tu pierdes!')
        derrotas += 1