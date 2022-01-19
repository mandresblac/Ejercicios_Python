#Ejercicio 6
'''Realiza una funcion llamada intermedio() que a partír de 2 números, devuelva un punto intermedio:
    NOTA: El número intermedio de dos números corresponde a la suma de los 2 números dividida entre 2.
comprueba el punto intermedio -12 y 24'''
'''
def intermedio(n1, n2):
    return (n1 + n2) // 2

n1=float(input("Inserte primer número: "))
n2=float(input("Inserte segundo número: "))

print("La media entre {} y {} es {}".format(n1, n2, intermedio(n1, n2)))
'''

#Ejercicio 7
'''Realiza una funcion llamada recortar() que reciba tres parametros. El primero es el número a recortar, el segundo es el limite 
inferior y el tercero el limite superior. La función tendra que cumplir lo siguiente:
    - Devolver el limite inferior si el número es menor que este
    - Devolver el limite superior si el número es mayor que este.
    - Devolver el número sin cambios si no se supera ningun limite.
Comprueba el resultado de recortar 15 entre los limites 0 y 10.'''

def recortar(numero, minimo, maximo):
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    return numero

print(recortar(15, 0, 10))

