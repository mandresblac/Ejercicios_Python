# Uso de los metodos .format y f en strings

nombres = input("Ingresa tu nombre: " )
apellidos = input("Ingresa tu apellido: ")

#Metodo .format
print("Hola {} {}, Bienvenido".format(nombres, apellidos))
print("Hola {1} {0}, Bienvenido".format(nombres, apellidos))

#Metodo f

print(f"Hola {nombres} {apellidos}, Bienvenido")
