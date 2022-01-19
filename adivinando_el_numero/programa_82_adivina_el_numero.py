
'''
Escriba un programa que piense un número de 1 a 10 de forma aleatoria y le pida al usuario que lo trate de adivinar.
El usuario puede intentar indefinidamente hasta que encuentre el número.

Un ejemplo de la ejecución del programa podría ser el siguiente, asumiendo que el número es 2:

Adivina el número: 5
Fallaste!

Adivina el número: 2
Felicitaciones, lo encontraste!
'''

import random

numero_secreto = random.randint(1, 10)
adivina = int(input("Adivina un número entre 1 y 10: "))

while True:
  if adivina == numero_secreto:
    print("Felicitaciones, lo encontraste")
    break
  else:
    print("Fallaste!")
    adivina = int(input("Adivina el número entre 1 y 10: "))

