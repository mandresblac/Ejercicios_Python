#Programa que solicita un nombre y una contraseña.

print()
while True:
    name = input('\t\t\t\t\t¿Quien eres?: ')
    if name != 'manuel':
        continue
    contraseña = int(input('\t\t\t\tHola Manuel. ¿Cual es la contraseña?: '))
    if contraseña == 10041980:
        break
print()
print('\t\t\t\t\t¡Acceso permitido! ¡BIENVENIDO!')
