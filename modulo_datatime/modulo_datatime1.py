#Modulo datetime para obtener fecha y hora.
#date = Fecha
#time = Hora

from datetime import date, datetime #Desde datatime se importa modulos date y datetime.

#Propiedades del modulo date:
print(f'Fecha actual: {date.today()}') #.today = Muestra la fecha actual.
print(f'Dia del mes: {date.today().day}') #date().today().day = Muestra el dia del mes actual.
print(f'Mes actual: {date.today().month}') #date.today().month = Muestra el número de mes actual.
print(f'Año actual: {date.today().year}') #date.today().year = Muestra el año actual.
print(f'Dia de la semana: {date.today().weekday()}') #date.today().weekday() = Muestra el dia de la semana, 0=Lun, 1=Mar, 2=Mier, 3=Jue, 4=Vie, 5=Sab, 6=Dom.


#Ejercicio1
mes={1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'}

dia_semana={0:'Lunes', 1:'Martes', 2:'Miercoles', 3:'Jueves', 4:'Viernes', 5:'Sabado', 6:'Domingo'}

print(f'Fecha actual: Hoy es {dia_semana[date.today().weekday()]} {str(date.today().day)} de {mes[date.today().month]} del año {str(date.today().year)}.')


#Propiedades del modulo datetime:
print()
print(f'Fecha y hora actual: {datetime.now()}') #.now = Muestra fecha y hora actual.
print(f'Segundos actuales: {datetime.now().second}')#datetime.now().second = Muestra los segundos actuales.|
print(f'Minutos actuales: {datetime.now().minute}')#datetime.now().minute = Muestra los minutos actuales.
print(f'Hora actual: {datetime.now().hour}')#datetime.now().hour = Muestra la hora actual en formato 24 horas.
print(f'Microsegundos actuales: {datetime.now().microsecond}')#datetime.now().microsecond = Muestra los microsegundos actuales.

#Metodo strftime
# strftime(string)  Metodo para formatear la hora que acepta un string.

# Fecha:
# %Y : Muestra el año cin 4 digitos.
# %m : Muestra el mes con 2 digitos.
# %d : Muestra el dia con 2 digitos.

# Hora:
# %H : Muestra la hora en formato 24 horas y 2 digitos.
# %M : Muestra los minutos actuales son 2 digitos.
# %S : Muestra los segundos actuales con 2 digitos.

print()
print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))



