import time

segundero = 0
maximo = 5

while True:
    time.sleep(1)
    segundero += 1
    print(segundero)

    if segundero == maximo:
        print("Se ha llegado al limite, rompiendo el bucle")
        break
    
