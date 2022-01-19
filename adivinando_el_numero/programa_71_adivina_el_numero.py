numero= 8
usuario= 0
while usuario != numero:
    usuario=int(input('Adivina cual es el número?: '))
    if usuario > numero:
        print('digita un número menor 👇')
    elif usuario < numero:
        print('digita un número mayor ☝')
    else:
        print()
        print('😀¡Correcto el número es {0}!😀 👍👍'.format(usuario))
