''' Programa para calcular el perímetro de una estructura y mostrarla en decímetros, para ello vamos a pedir tres datos en
diferentes escalas, uno en hectómetros, otro en decámetros y uno en metros. El algoritmo deberá hallar a cuanto equivale el valor
ingresado en hectómetros a decímetros, de decámetros a decímetros y de metros a decímetros, y sumar cada uno de los equivalentes
porque el algoritmo pide mostrar el resultado en decímetros.'''

hectometro = float(input("Inserte valor en hectometros: "))
decametro = float(input("Inserte valor en decametros: "))
metro = float(input("Inserte valor en metros: "))

hecto_a_decimetro = (hectometro * 1000) / 1
deca_a_decimetro = (decametro * 100) / 1
metro_a_decimetro = (metro * 10) / 1

s = hecto_a_decimetro + deca_a_decimetro + metro_a_decimetro

print()
print(f"{round(hectometro)} hectometros equivale a {round(hecto_a_decimetro)} decimetros")
print(f"{round(decametro)} decametros equivale a {round(deca_a_decimetro)} decimetros")
print(f"{round(metro)} metros equivale a {round(metro_a_decimetro)} decimetros")
print()
print(f"Resultado de la sumatoria en decimetros: {round(s)}")

