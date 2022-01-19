# Este programa dice si eres mayor o menos de edad.

print(" VERIFICACIÓN DE ACCESO ".center(136, "-"))

#Alternativa 1
edad_usuario=int(input("Introduce tu edad por favor: "))

if edad_usuario >= 18:
    print("Puede pasar, usted es mayor de edad")
elif edad_usuario >= 100:
    print("Edad incorrecta")
else:
    print("No puede pasar, usted es menor de edad")

print("El programa a finalizado")
