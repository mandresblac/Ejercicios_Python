# Funcion que muestra la tabla del multiplicar del 5

def tabla_del_5():
    for i in range(11):
        print(f"5 x {i} = {5 * i}")

print(" tabla de multiplicar del número 5 ".center(136, "-"))
print(tabla_del_5())

