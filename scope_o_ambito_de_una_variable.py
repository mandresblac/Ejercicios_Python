# Scope o ambito de una variable
# El ambito de una variable puede ser global o local.

mi_nombre= "Luis"

def imprime_nombre():
    global mi_nombre #Esta variable afecta a todo el programa por haberse declarado como global.
    mi_nombre="Martha"
    print("El nombre dentro de mi funcion es {}".format(mi_nombre))

imprime_nombre()
print("El nombre fuera de la funcion es {}".format(mi_nombre))
