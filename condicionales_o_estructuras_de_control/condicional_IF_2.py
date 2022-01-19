# Programa para sentencia if

print("Programa para saber en que etapa de la vida estas.")

edad = int(input("Inserta tu edad: "))

if edad <= 3:
    print("Eres un bebe.")

elif edad >= 4 and edad <= 12:
    print("Eres un niño")

elif edad >=13 and edad <= 17:
    print("Eres un Adolescente")

elif edad >= 18 and edad <=35:
    print("Eres Joven")

elif edad >= 36 and edad <= 59:
    print("Eres adulto")


elif edad >= 60 and edad <= 100:
    print("Eres adulto mayor")

else:
    edad > 100
    print("¡Valor incorrecto!")
