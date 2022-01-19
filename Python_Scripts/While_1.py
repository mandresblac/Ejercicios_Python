numeroMayor = -999999999
numero = int(input ("Introduzca un número o -1 para terminar:"))
while numero != -1:
   if numero > numeroMayor:
       numeroMayor = numero
   numero = int (input("Introduzca un número o -1 para terminar:"))
print("El número más grande es:", numeroMayor)