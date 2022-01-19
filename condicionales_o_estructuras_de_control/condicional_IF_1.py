#!/usr/bin/python
# -*- coding: UTF-8 -*-

print("PROGRAMA DE EVALUACIÓN DE NOTAS DE ALUMNOS")

nota_alumno = input("Introduce la nota del alumno: ")

def evaluacion(nota):
    valoracion = "!Aprobado!"
    if nota<=4.9:
        valoracion = "!Reprobado!"
    return valoracion

print(evaluacion(float(nota_alumno)))