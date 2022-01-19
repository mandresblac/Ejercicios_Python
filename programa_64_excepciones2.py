def evaluaEdad(edad):

    if edad<0:
        raise TypeError("No se permiten edades negativas")
    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuidate..."

#Metodo 1 para llamar a la funcion evaluaEdad
print(evaluaEdad(int(input("Ingresa tu edad: "))))

#Metodo 2 para llamar a la funcion evaluaEdad
numero= int(input("Ingresa tu edad: "))
print(evaluaEdad(numero))