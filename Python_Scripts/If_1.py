numeroSecreto  = 888
print(
    """
    +==============================+
    | Bienvenidos a mi juego:      |
    |Introduce un número entero    |
    |y trata de adivinar cuál es el|
    |número numeroSecreto          |
    |               SeaCCNA        |
    +==============================+
    """
)
n=int(input("Ingrese un número:"))
if numeroSecreto!=n:
  print("Ja, ja! ¡ Estás atrapado en mi bucle")
  n=int(input("ingresa un nuevo número:"))
else:
  print("El número es:", n)
  print("Lo has logrado, saliste del Bucle. www.seaccna.com")
