'''
nombre = input("Escribe tu nombre: ")
print(nombre * 5)
'''

euros = int(input("Ingresa un valor en euros: "))
interes = float(input("Ingresa un número para porcentaje: "))
años = int(input("Ingresa un número de años: "))

total = euros * (1 + (interes/100)) ** años

print(f"{euros} euros al {interes}% de interes anual en {años} años se convertiran en {round(total, 2)} euros")