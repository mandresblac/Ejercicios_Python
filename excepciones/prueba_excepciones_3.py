def evaluaEdad(edad):
    if edad<0:
        raise TypeError("No se permiten edades negativas") #Lansamiento de excepcion
    elif edad<=20:
        return "Eres muy joven"
    elif edad<=40:
        return "Eres joven"
    elif edad<=65:
        return "Eres maduro"
    elif edad<100:
        return "Cuídate..."

edad=int(input("Inserta tu edad: "))
print(evaluaEdad(edad))
