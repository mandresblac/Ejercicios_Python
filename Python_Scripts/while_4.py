while True:
    opcion = (input("""Elige una fruta para tu desayuno:
    1- Manzana
    2- Banano
    3- Nada
    : """))
    
    if opcion == "1":
        print("Has seleccionado manzana.")
        break
    elif opcion == "2":
        print("Has seleccionado Banano.")
        break
    elif opcion == "3":
        print("Has seleccionado Nada.")
        break
    else:
        print("Debes seleccionar una opción (1, 2 o 3)")
print("Programa terminado,que disfrutes tu desayuno.")