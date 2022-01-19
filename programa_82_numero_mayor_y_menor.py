# Programa para encontrar el numero mayor y menor wntre tres números con las funciones max() y min() que viene incorporadas por
# defecto es Python

numero1 = int(input("Ingresa el primer número:"))
numero2 = int(input("Ingresa el segundo número:"))
numero3 = int(input("Ingresa el tercer número:"))

# verifica cuál de los números es el mayor
# y pásalo a la variable de mayor número

numeroMayor = max(numero1,numero2,numero3)
numeroMenor = min(numero1,numero2,numero3)

# imprimir el resultado
print()
print("El número mayor es:", numeroMayor) 
print("El número menor es:", numeroMenor) 
