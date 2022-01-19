
print(" PROGRAMA DE EVALUACIÓN DE CALIFICACIÓN ALUMNOS ".center(136, "-"))

nota_alumno = float(input("Introduce la nota del alumno: "))

if nota_alumno <= 5.0:
    print("Insuficiente")
elif nota_alumno <= 6.0:
    print("Suficiente")
elif nota_alumno <= 7.0:
    print("Suficiente")
elif nota_alumno <= 9.0:
    print("Notable")
else:
    print("Sobresaliente")

