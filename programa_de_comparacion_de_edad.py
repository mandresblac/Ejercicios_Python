#Este programa compara la edad de 2 personas.

#Cabecera del programa
print()
print('\t' * 4, "PROGRAMA PARA COMPARAR LA EDAD DE 2 PERSONAS")
print()

#Recoleccion de datos
edad1 = int(input("\t\t\tInserte la edad de la primera persona, luego oprima la tecla enter: "))
edad2 = int(input("\t\t\tInserte la edad de la segunda persona, luego oprima la tecla enter:  "))
print()

#Operaciones
if edad1 < edad2:
    print('\t' * 5, "La primera persona es mas joven")
elif edad2 < edad1:
    print('\t' * 5, "La segunda persona es mas joven")
else:
    edad1 == edad2
    print('\t' * 5, "Ambos tienen la misma edad")

