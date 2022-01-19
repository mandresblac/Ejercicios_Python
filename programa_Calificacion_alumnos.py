# programa para calificacion notas alumnos
print()
print(" PROGRAMA PARA CALIFICAR ALUMNOS ".center(129, '*'))
print()

nota = float(input("\t\t\t Introduce la calificación del alumno, si son decimales utiliza el punto \".\": "))

while nota <= 0.0 or nota > 10:
    print('\t' * 3,'Has introducido un número incorrecto. ¡Vuelve a intentarlo!')
    nota = float(input("\t\t\t Introduce la calificación del alumno, si son decimales utiliza el punto \".\": "))

if nota <= 2.9:
    print('\t' * 5,"Insuficiente")
    print('\t' * 5,"¡OJO, vas muy mal! 😱😱")

elif nota >= 3.0 and nota <= 5.9:
    print('\t' * 5,"Deficiente😲😲")

elif nota >= 6.0 and nota <= 7.9:
    print('\t' * 5,"Aceptable")
    print('\t' * 5,"¡Debes esforzarte un poco mas! 🤔🤔")

elif nota >= 8.0 and nota <= 8.9:
    print('\t' * 5,"Bueno 🙂🙂")

elif nota >= 9.0 and nota <= 9.4:
    print('\t' * 5,"!Muy Bueno! 🙂🙂")

else:
    nota >= 9.5 and nota <= 10
    print('\t' * 5,"!Excelente!")
    print('\t' * 5,"¡Sigue así, y triunfaras! 😃😃")
