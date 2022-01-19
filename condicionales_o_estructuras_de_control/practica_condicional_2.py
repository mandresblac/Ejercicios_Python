print("Asignaturas optativas año 2020")
print("Informatica grafica \nPruebas de software \nUsabilidad y accesibilidad")

opcion = input("Escribe la asignatura escogida: ")

asignatura = opcion.lower() #Transforma a minusculas lo insertado en opción.

if asignatura in("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida " + asignatura)
else:
    print("la asignatura escogida no esta contemplada.")