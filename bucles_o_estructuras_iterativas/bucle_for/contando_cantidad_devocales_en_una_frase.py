# Este programa cuenta la cantidad de vocales que hay en una frase, no importa si estan repetidas.

frase=input("Ingrese una frase: ")
cantidad=0 #Contador que lleva la cuenta de la cantidad de vocales que se inicializa en 0.
for x in frase:
    if x in "aeiou":
        cantidad += 1 # cantidad = cantida + 1
print("Esta frase tiene {} vocales".format(cantidad))

