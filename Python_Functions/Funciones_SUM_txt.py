def mensaje():
    	print("Ingrese un valor, para definir A, B y C. Consecutivamente.")

mensaje()
a = int(input("A: "))
mensaje()
b = int(input("B: "))
mensaje()
c = int(input("C: "))

print(a, "+", b, "+", c, "=", a + b + c)