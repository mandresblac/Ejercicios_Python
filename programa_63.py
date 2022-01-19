def devuelve_ciudades(*ciuades):
    for elemento in ciuades:
        #for subElemento in elemento:
            yield from elemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Vilbao", "Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))



