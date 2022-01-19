#Ejemplo de concatenacion de operadores de comparación

salario_presidente= int(input("Introduce salario del presidente de la compañia: "))
print("Salarios presidente: ", str(salario_presidente))

salario_director= int(input("Introduce salario del direcor de la compañia: "))
print("Salarios presidente: ", str(salario_director))

salario_jefe_de_area= int(input("Introduce salario del jefe del area de la compañia: "))
print("Salarios presidente: ", str(salario_jefe_de_area))

salario_administrativo= int(input("Introduce salario del administrativo de la compañia: "))
print("Salarios presidente: ", str(salario_administrativo))

if salario_administrativo<salario_jefe_de_area<salario_director<salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en esta empresa")

