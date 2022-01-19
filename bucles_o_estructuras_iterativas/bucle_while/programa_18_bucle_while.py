print("Bienvenido al menu interactivo")
while (True):
    print("""¿Que quires hacer? Escribe una opcion:
    1) Saludar.
    2) Sumar dos números.
    3) Salir.""")
    opcion = input(":")
    if opcion == "1":
        print("Hola, espero que te lo estes pasando bien.")
        print()
    elif opcion == "2":
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print("El resultado de la suma es: ", n1 + n2)
        print()
    elif opcion == "3":
        print("Hasta luego, ha sido un placer ayudarte.")
        break
    else:
        print()
        print("Comando desconocido, vuelve a intentarlo.")
