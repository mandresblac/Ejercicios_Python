'''
Como seguramente sabrás, debido a algunas razones astronómicas, el año puede ser bisiesto o común. Los primeros tienen una
duración de 366 días, mientras que los últimos tienen una duración de 365 días.

Desde la introducción del calendario gregoriano (en 1582), se utiliza la siguiente regla para determinar el tipo de año:

Si el número del año no es divisible entre cuatro, es un año común.
De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
De lo contrario, si el número del año no es divisible entre 400, es un año común.
De lo contrario, es un año bisiesto.

El código debe mostrar uno de los dos mensajes posibles, que son "Año bisiesto" o "Año común", según el valor ingresado.

Sería bueno verificar si el año ingresado cae en la era gregoriana y emitir una advertencia de lo contrario: "No dentro del período
del calendario gregoriano". Consejo: utiliza los operadores != y %.

Prueba tu código con los datos que hemos proporcionado:
Entrada de muestra: 2000
Resultado esperado: Año bisiesto

Entrada de muestra: 2015
Resultado esperado: Año común

Entrada de muestra: 1999
Resultado esperado: Año común

Entrada de muestra: 1996
Resultado esperado: Año bisiesto

Entrada de muestra: 1580
Resultado esperado: No dentro del período del calendario gregoriano
'''

año = int(input("Introduzca un año: "))

if año >= 1582: #si el año ingresado cae en la era gregoriana
    if año % 4 != 0: #Si el número del año no es divisible entre cuatro, es un año común.
        print("Año común")
    elif año % 100 != 0: #De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
        print("Año bisiesto")
    elif año % 400 != 0: #De lo contrario, si el número del año no es divisible entre 400, es un año común.
        print("Año común")
    else: #De lo contrario, es un año bisiesto.
        print("Año bisiesto")
else: #si el año ingresado no cae en la era gregoriana
    print("No dentro del período del calendario gregoriano")

