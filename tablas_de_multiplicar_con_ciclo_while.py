
def imprimir_tabla(numero):
    #Se supone que las tablas llegan hasta el 10
    limite = 10
    #Comenzar en 1
    contador = 1
    while contador <= limite:
        resultado = contador * numero
        print('{} x {} = {}'.format(numero, contador, resultado))
        #Incrementar el contador para no caer en un ciclo infinito.
        contador += 1

print()
print(' TABLAS DE MULTIPLICAR '.center(129, '*'))

digito=int(input('Ingrese un número: '))
print()

#Invocacion de la funcion
print("Tabla del número {}".format(digito))
imprimir_tabla(digito)

