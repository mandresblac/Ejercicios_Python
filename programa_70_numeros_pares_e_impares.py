#Programa que nos muestra los números pares e impares.

n=int(input('Inserte un número entero desde donde arranca la secuencia: '))
hasta=int(input('Inserte un número entero hasta donde quiere que llegue la secuencia: '))

while n < hasta + 1: #Bucle while
    if (n % 2 ) == 0: #Condicional #Condicional
        print('{} es número par'.format(n))
    else:
        print('{} es número impar'.format(n))
    n +=1 # n = n +1

print()
print('¡Programa finalizado!')




