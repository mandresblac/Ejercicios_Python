#Metodos de lista

animales=['Perro', 'Gato', 'Caballo', 'Gallina']
animales.append('Pato') #Inserta un elemento al final de la lista
animales.remove('Perro') #Elimina un elemento de la lista
animales.extend(['Mariposa', 'Hormiga', 'Vaca']) #Inserta varios nuevos elementos al final de la lista
animales.insert(0, 'Raton') #Inserta un nuevo elemento en la posicion que le indiquemos en la lista

for i in animales:
    print(i, end=', ')
print()
