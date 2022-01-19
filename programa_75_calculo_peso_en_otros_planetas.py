#Programa para calcular el peso en otros planetas

print()
print(" PROGRAMA PARA CALCULAR EL PESO EN OTROS PLANETAS ".center(129, "*"))
print()

peso=float(input("Ingrese su peso en la tierra: "))
print()
planeta=int(input("PLANETAS \n1- Marte \n2- Jupiter \n3- Saturno \nEscoja el número del planeta: "))

g_tierra = 9.8
g_marte = 3.7
g_jupiter = 24.8
g_saturno = 10.44

peso_final_marte= (peso * g_marte) / g_tierra
peso_final_jupiter= (peso * g_jupiter) / g_tierra
peso_final_saturno= (peso * g_saturno) / g_tierra

if planeta == 1:
    print("Tu peso en Marte es de {} Kg".format(round(peso_final_marte, 2)))
elif planeta == 2:
    print("Tu peso en Jupiter es de {} Kg".format(round(peso_final_jupiter, 2)))
else:
    planeta == 3
    print("Tu peso en Saturno es de {} Kg".format(round(peso_final_saturno, 2)))
