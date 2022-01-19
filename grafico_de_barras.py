from turtle import Screen, Turtle

print("Grafico de barras")

#Recoleccion de datos
alumnos = int(input("Escriba el número de alumnos que hay en su curso, luego oprima la tecla enter: "))
num1 = int(input("Inserte el numero de alumnos con calificacion suspenso, luego oprima la tecla enter: "))
num2 = int(input("Inserte el numero de alumnos con calificacion aprobado, luego oprima la tecla enter: "))
num3 = int(input("Inserte el numero de alumnos con calificacion notable, luego oprima la tecla enter: "))
num4 = int(input("Inserte el numero de alumnos con calificacion sobresaliente, luego oprima la tecla enter: "))

#operaciones
a = ((num1 * 100) / alumnos)
b = ((num2 * 100) / alumnos)
c = ((num3 * 100) / alumnos)
d = ((num4 * 100) / alumnos)

longitud1 = num1
longitud2 = num2
longitud3 = num3
longitud4 = num4


pantalla = Screen()
pantalla.setup(600, 500)
pantalla.screensize(400, 200)
tortuga = Turtle()
tortuga.speed(0)
tortuga.pensize(1)
tortuga.pencolor("blue")

#Dibujo barra suspensos
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

#Escribir el texto para los suspensos
tortuga.penup()
tortuga.forward(30)
tortuga.write("suspensos")

#Dibujo barra aprobados
tortuga.backward(30)
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

#Escribir el texto para los aprobados
tortuga.penup()
tortuga.forward(30)
tortuga.write("aprobados")

#Dibujo barra notables
tortuga.backward(30)
tortuga.left(90)
tortuga.forward(110)
tortuga.pendown()
tortuga.forward(60)
tortuga.left(90)
tortuga.forward(longitud3)
tortuga.left(90)
tortuga.forward(60)
tortuga.left(90)
tortuga.forward(longitud3)

#Escribir el texto para los notables
tortuga.penup()
tortuga.forward(30)
tortuga.write("notables")

#Dibujo barra sobresalientes
tortuga.backward(30)
tortuga.left(90)
tortuga.forward(110)
tortuga.pendown()
tortuga.forward(60)
tortuga.left(90)
tortuga.forward(longitud4)
tortuga.left(90)
tortuga.forward(60)
tortuga.left(90)
tortuga.forward(longitud4)

#Escribir el texto para los sobresalientes
tortuga.penup()
tortuga.forward(30)
tortuga.write("sobresalientes")

#Escribir el texto de porcentaje para los sobresalientes
tortuga.backward(30)
tortuga.backward(longitud4)
tortuga.left(180)
tortuga.forward(10)
tortuga.right(90)
tortuga.forward(30)
tortuga.write(f"{num4} %")

#Salir cuando se pulse el boton de la ventana
pantalla.exitonclick()
