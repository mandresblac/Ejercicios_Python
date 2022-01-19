#Programa para calcular la estatura (dada en pies y pulgadas) en centimetros.

# 1 pie (ft) = 30.48 cm.
# 1 pulgada (") = 2.54 cm.

print()
print('PROGRAMA PARFA CALCULAR LA ESTATURA DADA EN PIES Y PULGADAS A CENTIMETROS')
pies = float(input('Iserte su estatura en pies (ft), luego oprima la tecla enter: '))
pulgadas = float(input('Iserte su estatura en pulgadas (\"), luego oprima la tecla enter): '))

cm =  pies * 30.48
cm += pulgadas *2.54

print('Su estatura es {} cm'.format(cm))