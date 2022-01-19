#Un Diccionario esta conformado por una clave y un valor, es decir  Clave:Valor

mi_diccionario={'Nombre':'Pedro', 'Apellido':'Torres', 'Edad':32}
mi_diccionario.update({'Nacionalidad':'Colombiana'})  #.update metodo para agregar un elemento (clave:valor) al diccionario.
clave=mi_diccionario.keys() #.keys muestra las claves del diccionario.
valor=mi_diccionario.values()  #.values muestra los valores del diccionario.
#valor_unico=mi_diccionario.get() #.get muestra un unico valor del diccionario.
cantidad_elementos=mi_diccionario.items() #.items devuelve el total de elementos dentro del diccionario.

for clave, valor in cantidad_elementos:
    print('{} : {}'.format(clave, valor))
print(cantidad_elementos)