#!/usr/bin/python
# -*- coding: UTF-8 -*-


import calendar

print()
print(' CALENDARIO AÑO-MES '.center(134, '*'))
año=int(input('Escriba el año: '))
mes=int(input('Escriba el mes: '))

print()
print(calendar.month(año, mes))

'''
cl1=calendar.TextCalendar()
calendario_sep=cl1.formatmonth(2009, 9)
print(calendario_sep)

cl2=calendar.TextCalendar()
calendario_2009=cl2.formatyear(2009)
print(calendario_2009)

for i in calendar.day_name:
    print(i, end=' ')
print()


dias=['Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa', 'Do']
enero= dict(zip(range(1, 32), dias * 5))
febrero = dict(zip(range(1, 31), dias * 5))


mes=input('Ingrese el mes deseado: ')
x=mes.upper()

if x == 'ENERO':
    print('{0} \n{1}'.format(x, enero))
else:
    print('{0} \n{1}'.format(x, febrero))'''
