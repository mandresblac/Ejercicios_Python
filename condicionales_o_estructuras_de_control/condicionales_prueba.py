print()
print(" Programa de evaluacion de notas de alumnos ".center(136, "*"))

def evaluacion(nota):
    valoracion= "aprobado"
    if nota < 5:
        valoracion="Suspenso"
    return valoracion

nota_alumno = float(input("Introduce la nota del alumno: "))

print(evaluacion(nota_alumno))
