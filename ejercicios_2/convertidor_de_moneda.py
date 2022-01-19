print()
print("CONVERTIDOR DE MONEDA")
opcion = int(input("""Seleccione un número para el tipo de moneda y luego pulse la tecla enter:
1- Pesos.
2- Dolares.
3- Euros.
4- Libras esterlinas.
:"""))

valor = int(input("Ahora inserte en valor: "))

if opcion == 1:
    dolar = 3872
    print(f"$ {valor} pesos equivalen a {round((valor * 1) / dolar, 2)} Dolares")
   euro = 4536
    print(f"$ {valor} pesos equivalen a {round((valor * 1) / euro, 2)} Euros")
    libra = 5000
    print(f"$ {valor} pesoso equivalen a {round((valor * 1) / libra, 2)} Libras esterlinas")
elif opcion == 2:
    peso = 3872
    print(f"$ {valor} dolares equivalen a {round((valor * peso) / 1, 2)} Pesos")
    euro = 0.85
    print(f"$ {valor} dolares equivalen a {round((valor * euro) / 1, 2)} Euros")
    libra = 0.77
    print(f"$ {valor} dolares equivalen a {round((valor * libra) / 1, 2)} Libras esterlinas")
elif opcion == 3:
    peso = 4536
    print(f"$ {valor} Euros equivalen a {round((valor * peso) / 1, 2)} Pesos")
    dolar= 1.17
    print(f"$ {valor} Euros equivalen a {round((valor * dolar) / 1, 2)} Dolares")
    libra = 0.91
    print(f"$ {valor} Euros equivalen a {round((valor * libra) / 1, 2)} Libras esterlinas")
else:
    opcion == 4
    peso = 5010
    print(f"$ {valor} libras esterlinas equivalen a {round((valor * peso) / 1, 2)} Pesos")
    dolar = 1.29
    print(f"$ {valor} Libras esterlinas equivalen a {round((valor * dolar) / 1, 2)} Dolares")
    euro = 1.10
    print(f"$ {valor} Libras esterlinas equivalen a {round((valor * euro) / 1, 2)} Euros")



