contador = 0
miEmail = input('Escribe tu direccion de email, luego oprime enter: ')

for i in miEmail:
    if(i == '@' or i == '.'):
        contador = contador + 1

if contador == 2:
    print('Email correcto.')
else:
    print('Email incorrecto.')

