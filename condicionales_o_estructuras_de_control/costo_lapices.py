'''
Realice un algoritmo para determinar cuánto se debe pagar por equis cantidad de lápices considerando que si son 1000 o más el costo
es de 85¢; de lo contrario, el precio es de 90¢
'''

print()
print(" PROGRAMA PARA CALCULAR EL COSTO DE LAPICES ".center(136, "-"))
print()
print('''Si son mas de 1.000 lapices, costo por lapiz es de 85 centavos. \nSi son menos de 1.000, costo por lapiz es de 90 centavos.''')

print()
cantidad_lapices =int(input("Ingrese la cantidad de lapices que va a comprar: "))

if cantidad_lapices >= 1000:
    pag1 = cantidad_lapices * 0.85
    print(f"El pago es: {round(pag1, 1)} pesos")
else:
    pag2 = cantidad_lapices * 0.95
    print(f"El pago es: {round(pag2, 1)} pesos")

