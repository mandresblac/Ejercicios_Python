#Ejercicio bucle for

numeros=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
indice=0
'''
while (indice < len(numeros)):
    print(numeros[indice], end=" ")
    indice += 1'''

'''
for i in numeros:
    print(i, end=" ")'''

for numero in numeros:
    numeros[indice] *= 10
    indice += 1
print(numeros)
