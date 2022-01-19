
# Ejercicio 1
'''
def dibujar_tabla_del_5():
    for i in range(10 + 1):
        print("5 * ", i, "=", i * 5)

dibujar_tabla_del_5()
'''

# Ejercicio 2
'''
def test():
    return 'Una cadena retornada'
print(test())
c = test()
print(c)
'''

# Ejercicio 3
'''
def test():
    return [1, 2, 3, 4, 5]

l = test()
print(l[-1])
'''

#Ejercicio 4
'''
Crear una funcion que sume 2 números y retorne su resultado
'''
'''
def suma (num1, num2):
    resultado= num1 + num2
    return resultado

num1 = int(input("Inserte primer número: "))
num2 = int(input("Inserte segundo número: "))

print("La suma de {} + {} es igual a {}".format(num1, num2, suma(num1, num2)))
print(f"La suma de {num1} + {num2} es igual a {suma(num1, num2)}")
'''

#Ejercicio 5
'''
Crear una funcion que reste 2 números y retorne su resultado

def  resta(num1, num2):
    resultado= num1 - num2
    return resultado

num1 = int(input("Inserte primer número: "))
num2 = int(input("Inserte segundo número: "))

print(f'{num1} - {num2} = {resta(num1, num2)}')
print("{} - {} = {}".format(num1, num2, resta(num1, num2)))
'''

#Ejercicio 6
'''Realiza una función llamada area_rectangulo() que devuelva el área del cuadrado a partir de una base y una altura. Cálcula el
área de un rectangulo de 15 de base y 10 de altura.
NOTA: El área de un rectangulo se obtiene al multiplicar la base por la altura.'''

'''
def area_rectangulo(base, altura):
    area = base * altura
    return area

base = int(input("Inserta la base del rectangulo: "))
altura = int(input("Inserta la altura del rectangulo: "))

print("El area del rentangulo es {}".format(area_rectangulo(base, altura)))
'''

#Ejercicio 7
'''
Realiza una funcion llamada area_circulo() que devuelva el área de un circulo a partir de un radio. Calcula el área de un circulo
de 5 de ancho.
Nota: El área de un circulo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi= 3.14159 o importando
el modulo math:

    import math
    print(math.pi)
    >3.1415...'''

'''
import math

def area_circulo(radio):
    area = (radio ** 2)* math.pi
    return area

radio = float(input("Inserte el radio del circulo: "))
print(f"El area del circulo de radio {radio} es: {round(area_circulo(radio), 2)}")
print("El area del circulo de radio {} es: {}".format(radio, round(area_circulo(radio), 2)))
'''

#Ejercicio 8
'''Realiza una funcion llamada relación() que a partir de 2 números cumpla lo siguiente:
    - Si el primer número es mayor que el segundo, debe devolver 1.
    - Si el primer número es menor que el segundo, debe devolver -1.
    - Si ambos números son iguales, debe devolver un 0.
Comprueba la relación entre los números: 5 y 10, 10 y 5, 5 y 5.'''
'''
def relacion(n1, n2):
    if n1 > n2:
        return 1
    elif n1 < n2:
        return -1
    else:
        n1 == n2
        return 0

n1 = int(input("Inserte primer número: "))
n2 = int(input("Inserte segundo número: "))

print(relacion(n1, n2))
'''

