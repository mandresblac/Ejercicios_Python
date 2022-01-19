def divide():
    try:
        op1=(float(input("Introduce el primer número: ")))
        op2=(float(input("Introduce el segundo número: ")))
        print(f"La división es: {str(op1/op2)}")
    except ValueError:
        print("EL valor introducido es erróneo")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    finally:
        print("Cálculo finalizado")

divide()

