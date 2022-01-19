from turtle import Screen, Turtle

print("Grafico de pastel")

#Recoleccion de datos
num1 = int(input("Inserte el numero de alumnos con calificacion suspenso, luego oprima la tecla enter: "))
num2 = int(input("Inserte el numero de alumnos con calificacion aprobado, luego oprima la tecla enter: "))
num3 = int(input("Inserte el numero de alumnos con calificacion notable, luego oprima la tecla enter: "))
num4 = int(input("Inserte el numero de alumnos con calificacion sobresaliente, luego oprima la tecla enter: "))

#Calificaciones
suspensos = num1
aprobados = num2
notables = num3
sobresalientes = num4

#Radío del circulo
radio = 300

pantalla = Screen()
tortuga = Turtle()
tortuga.speed(0)

#Dibujo del circulo exterior
tortuga.penup()
tortuga.goto(0, -radio)
tortuga.pendown()
tortuga.circle(radio)
tortuga.penup()
tortuga.home()
tortuga.pendown()

#Dibujo de la linea para los suspensos
angulo = 360 * suspensos / 100
tortuga.left(angulo)
tortuga.forward(radio)
tortuga.backward(radio)

#Escribir el texto para los suspensos
tortuga.penup()
tortuga.right(angulo / 2)
tortuga.forward(radio / 2)
tortuga.write("suspensos")
tortuga.backward(radio / 2)
tortuga.left(angulo / 2)
tortuga.pendown()

#Dibujo de la linea para los aprobados
angulo = 360 * aprobados / 100
tortuga.left(angulo)
tortuga.forward(radio)
tortuga.backward(radio)

#Escribir texto para los aprobados
tortuga.penup()
tortuga.right(angulo / 2)
tortuga.forward(radio / 2)
tortuga.write("aprobados")
tortuga.backward(radio / 2)
tortuga.left(angulo / 2)
tortuga.pendown()

#Dibujo de la linea para los notabes
angulo = 360 * notables / 100
tortuga.left(angulo)
tortuga.forward(radio)
tortuga.backward(radio)

#Escribir texto para los notables
tortuga.penup()
tortuga.right(angulo / 2)
tortuga.forward(radio / 2)
tortuga.write("notables")
tortuga.backward(radio / 2)
tortuga.left(angulo / 2)
tortuga.pendown()

#Dibujo de la linea para los sobresalientes
angulo = 360 * sobresalientes / 100
tortuga.left(angulo)
tortuga.forward(radio)
tortuga.backward(radio)

#Escribir texto para los sobresalientes
tortuga.penup()
tortuga.right(angulo / 2)
tortuga.forward(radio / 2)
tortuga.write("sobresalientes")
tortuga.backward(radio / 2)
tortuga.left(angulo / 2)
tortuga.pendown()
tortuga.hideturtle()

#Salir cuando se pulse el boton de la ventana
pantalla.exitonclick()
