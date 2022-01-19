from datetime import datetime

fecha = datetime.now()  #Fecha y hora actual


print(fecha)           # AAA-MM-DD HH:MM:SS.microsegundos
print(fecha.year)      # Año
print(fecha.month)     #  Mes
print(fecha.day)       # dia

print()
print(fecha.hour)       # Hora
print(fecha.minute)     # Minutos
print(fecha.second)     # Segundos
print(fecha.microsecond) # Microsegundos

#Ejemplo 1:
print('{}:{}:{}'.format(fecha.hour, fecha.minute, fecha.second))

#Ejemplo 2:
print('{}/{}/{}'.format(fecha.day, fecha.month, fecha.year))


#Metodo strftime(format), permite especificar como se muestra la fecha y hora:

#Codigos de formateo:
# Fecha:
# %Y : Muestra el año con 4 digitos.
# %m : Muestra el mes con 2 digitos.
# %d : Muestra el dia con 2 digitos.

# Hora:
# %H : Muestra la hora en formato 24 horas y 2 digitos.
# %M : Muestra los minutos actuales son 2 digitos.
# %S : Muestra los segundos actuales con 2 digitos.

fecha = datetime.now()    # Fecha y hora actual

print()
print(fecha.strftime("Las %H:%M:%S del %A %d de %B del %Y"))
