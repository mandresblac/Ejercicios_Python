empresa = {
    1:['Angela Cardenas', 'Marcos Torres', 'Nelson Diaz', 'Carolina Restrepo'],
    2:['Jua Diego Perez', 'Pilar Torres', 'Diana Gonsalez', 'Monica Lopez'],
    3:['Hector Rodrigeuz', 'Andres Sanchez', 'Gustavo Velez', 'Lina florez'],
    4:['Esteban Agudelo', 'Rafael Novoa', 'Esperanza Castro', 'Laura Gomez']
    }

Valor=empresa.values()

print()
print(' PROGRAMA PARA SABER LOS EMPLEADOS QUE TIENE UNA EMPRESA EN CADA DEPARTAMENTO'.center(134, '-') )
print('''Departamentos:
1. Sistemas
2. Contabilidad
3. Contratos
4. Compras''')

print()
departamento = int(input("Seleccione el número del departamento: "))

for i in empresa.get(departamento):
    print('Los empleados este departamento son: {}'.format(i))