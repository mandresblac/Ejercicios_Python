from turtle import Screen, Turtle
print()
print("\t\t\t\t\tGRAFICO DE BARRAS")
print()

#Recoleccion de datos
alumnos = int(input("\tinserte el número de alumnos que hay en su curso, luego oprima la tecla enter: "))
num1 = int(input("\tInserte número de alumnos con calificacion Deficiente, luego oprima la tecla enter: "))
num2 = int(input("\tInserte número de alumnos con calificacion Aceptable, luego oprima la tecla enter: "))
num3 = int(input("\tInserte número de alumnos con calificacion Buena, luego oprima la tecla enter: "))
num4 = int(input("\tInserte número de alumnos con calificacion Excelente, luego oprima la tecla enter: "))

#operaciones
a = ((num1 * 100) // alumnos)
b = ((num2 * 100) // alumnos)
c = ((num3 * 100) // alumnos)
d = ((num4 * 100) // alumnos)


longitud1 = num1
longitud2 = num2
longitud3 = num3
longitud4 = num4

pantalla = Screen()
pantalla.setup(600, 500)
pantalla.screensize(400, 200)
tortuga = Turtle()
tortuga.speed(0)
tortuga.pensize(1.5)
tortuga.pencolor("blue")

#Dibujo barra deficiente
tortuga.penup()
tortuga.backward(195)
tortuga.pendown()
tortuga.forward(60)
tortuga.left(90)
tortuga.forward(longitud1)
tortuga.left(90)
tortuga.forward(60)
tortuga.left(90)
tortuga.forward(longitud1)

#Escribir el texto inferior para los deficientes
tortuga.penup()
tortuga.forward(20)
tortuga.write("Deficiente")

#Escribir el texto superior para los deficientes
tortuga.left(180)
tortuga.penup()
tortuga.forward(20)
tortuga.forward(longitud1)
tortuga.forward(5)
tortuga.right(90)
tortuga.forward(20)
tortuga.write(f"{a} %")

#Dibujo barra aceptable
tortuga.backward(20)
tortuga.right(90)
tortuga.forward(5)
tortuga.forward(longitud1)
tortuga.left(90)
tortuga.forward(110)
tortuga.pendown()
tortuga.forward(60)
tortuga.left(90)
tortuga.forward(longitud2)
tortuga.left(90)
tortuga.forward(60)
tortuga.left(90)
tortuga.forward(longitud2)

#Escribir el texto inferior para los aceptable
tortuga.penup()
tortuga.forward(20)
tortuga.write("Aceptable")

#Escribir el texto superior para los aceptable
tortuga.left(180)
tortuga.penup()
tortuga.forward(20)
tortuga.forward(longitud1)
tortuga.forward(5)
tortuga.right(90)
tortuga.forward(20)
tortuga.write(f"{b} %")

#Dibujo barra Bueno
tortuga.backward(20)
tortuga.right(90)
tortuga.forward(5)
tortuga.forward(longitud1)
tortuga.left(90)
tortuga.forward(110)
tortuga.pendown()
tortuga.forward(60)
tortuga.left(90)
tortuga.forward(longitud2)
tortuga.left(90)
tortuga.forward(60)
tortuga.left(90)
tortuga.forward(longitud2)

#Escribir el texto inferior para los Bueno
tortuga.penup()
tortuga.forward(20)
tortuga.write("Bueno")

#Escribir el texto superior para los bueno
tortuga.left(180)
tortuga.penup()
tortuga.forward(20)
tortuga.forward(longitud1)
tortuga.forward(5)
tortuga.right(90)
tortuga.forward(20)
tortuga.write(f"{c} %")

#Dibujo barra Excelente
tortuga.backward(20)
tortuga.right(90)
tortuga.forward(5)
tortuga.forward(longitud1)
tortuga.left(90)
tortuga.forward(110)
tortuga.pendown()
tortuga.forward(60)
tortuga.left(90)
tortuga.forward(longitud2)
tortuga.left(90)
tortuga.forward(60)
tortuga.left(90)
tortuga.forward(longitud2)

#Escribir el texto inferior para los Excelente
tortuga.penup()
tortuga.forward(20)
tortuga.write("Excelente")

#Escribir el texto superior para los Excelente
tortuga.left(180)
tortuga.penup()
tortuga.forward(20)
tortuga.forward(longitud1)
tortuga.forward(5)
tortuga.right(90)
tortuga.forward(20)
tortuga.write(f"{d} %")
tortuga.hideturtle()

#Resultados
print()
print(f"\t{num1} alumnos con calificacion Deficiente son el {a}% de {alumnos}. ")
print(f"\t{num2} alumnos con calificacion Aceptable son el {b}% de {alumnos}. ")
print(f"\t{num3} alumnos con calificacion Buena son el {c}% de {alumnos}. ")
print(f"\t{num4} alumnos con calificacion Excelente son el {d}% de {alumnos}. ")
print()
print("\tGracias por usar el programa. ¡Adiós!")

#Salir cuando se pulse el boton de la ventana
pantalla.exitonclick()
