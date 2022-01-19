'''
def a():
    print('a() comienza')
    b()
    d()
    print('q() regresa')

def b():
    print('b() comienza')
    c()
    print('a() devuelve')

def c():
    print('c() comienza')
    print('c() devuelve')

def d():
    print('d() comienza')
    print('d() devuelve')

a()
'''

'''
def spam ():
    huevos = 31337
spam ()
print(huevos)
'''

def spam(dividePor):
    try:
        return 42 /dividePor
    except ZeroDivisionError:
        print('Error: Invalid argument')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))