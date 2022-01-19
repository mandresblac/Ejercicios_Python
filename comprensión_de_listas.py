#Ejercicios de Comprension de listas

# Ejercicio 1
# Ciclo for comun y corriente
for i in range(1, 11):
    print(i * 2, end=" ")
print()

# Repetimos el ejercicio anterior pero con COMPRENSION DE LISTAS
dobles = [n*2 for n in range(1, 11)]
print(dobles)


# Ejercicio 2
# Crear una lista por comprension que contenga 5 cadenas de caracteres con uno, dos, tres, cuatro y cinco 
# asteriscos
cadenas = ["*" * n for n in range(1, 6)]
print(cadenas)


# Ejercicio 3
# Crear una lista con el cuadrado  de cada uno de los elementos de la lista números.
numeros = [2, 3, 5, 8, 9]

cuadrados = [n ** 2 for n in numeros]
print(cuadrados)


# Ejercicio 4
# Crear una lista con cada una de las letras de la palabra guardada en la variable cadena.
cadena = "artefacto"

# Con un ciclo for normal seria:
letras = []
for letra in cadena:
    letras.append(letra)
print(letras)

# Con una lista por comprensión seria:
letras = [letra for letra in cadena]
print(letras)


# Ejercicio 5
# Crear una lista con las iniciales de las palabras que se encuentran en la lista palabras
palabras = ["Casa", "Mesa", "Silla", "Puerta", "Ventana"]

# Con un ciclo for normal seria:
iniciales = []
for p in palabras:
    iniciales.append(p[0])
print(iniciales)

# Con una lista por comprensión seria:
iniciales = [p[0] for p in palabras]
print(iniciales)


# Ejercicio 6
# Crear una lista que contenga solo los núneros pares que se en cuentran en la lista datos.
datos = [14, 18, 21, 29, 36, 41, 58, 63, 74]

# Con un ciclo for normal seria:
pares=[]
for i in datos:
    if i % 2 == 0:
        pares.append(i)
print(pares)

# Con una lista por comprensión seria:
pares = [i for i in datos if i % 2 == 0]
print(pares)
