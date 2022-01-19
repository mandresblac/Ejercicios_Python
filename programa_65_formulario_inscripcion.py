#Formulario de inscripcion

print()
print(' FORMULARIO DE INSCRIPCION '.center(134, '*'))
print()


nombre=input('Escriba su nombre completo: ')
apellido=input('Escriba sus apellidos completos: ')
domicilio=input('Escriba la ciudad donde reside: ')
cedula=int(input('Escriba su número de cedula: '))

print(f'Yo {nombre} {apellido}, vecino de la ciudad de {domicilio}, con CC. No {cedula}')