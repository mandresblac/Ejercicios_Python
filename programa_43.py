'''
#Este programa separa los números pares e impares en el rango de 1 a 10:
x = 1

while x < 11:
    if x % 2 == 0:
        print(str(x) + ' es par.')
    else:
        print(str(x) + ' es impar.')
    
    x += 1
'''

'''
#Uso de break
list = [2, 3, 4, 5, 6, 7]

for x in list:
    if(x % 2 == 1 and x > 4):
        print(x)
        break
'''


#Declaracion return dentro de una funcion.

def max(x,y):
    if x >= y:
        return x
    else:
        return y

print(max(4, 7))

z = max(8, 5)
print(z)