def iva():
    '''Funcion basica para el calculo del iva'''
    iva = 19 
    costo = int(input("¿Cual es el monto a calcular?: "))
    calculo = (costo * iva) // 100
    print(f"El calculo del iva es: $ {str(calculo)}")
    #print("El calculo del iva es: " + str(calculo))
iva()
