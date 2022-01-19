#Programa para calcular la estatura (dada en centimetros) a metros, pies y pulgadas.

# 1 metro (m) = 100 cm.
# 1 pie (ft) = 30.48 cm.
# 1 pulgada (") = 2.54 cm.

print()
print('*'* 129)
print('\t' * 5, 'PROGRAMA PARA CALCULAR LA ESTATURA (DADA EN', '\n', '\t' * 5, '  CENTIMETROS) A METROS, PIES Y PULGADAS')
print('*'* 129)
print()

cm = float(input('Inserte su estatura en centimetros (cm), luego oprima la tecla enter: '))

metro = ((cm * 1) / 100)
pie = ((cm * 1) / 30.48)
pulgadas =((cm * 1) / 2.54)

print()
print('Su estatura en metros es: ' + str(round(metro, 2)) + ' m')
#print(f'Su estatura en metros es: {round(metro, 2)} m')
print('Su estatura en pies es: ' + str(round(pie, 2)) + ' ft')
#print(f'Su estatura en pies es: {round(pie, 2)} ft')
print('Su estatura en pulgadas es: ' + str(round(pulgadas, 2)) + ' "')
#print(f'Su estatura en pulgadas es: {round(pulgadas, 2)} \"')

print()
print('*'* 129)
print('\t' * 6,'FIN DEL PROGRAMA')
print('*'* 129)