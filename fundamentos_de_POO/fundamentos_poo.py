class Coche():

    #Metodo constructor que da un estado inicial a los objetos que pertenecen a la clase Coche.
    def __init__(self):
        #Propiedades de la clase Coche
        self.__largo_chasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

    #Comportamientos o metodos de la clase Coche
    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos
        
        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()
        
        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha."
        
        elif(self.__enmarcha and chequeo == False):
            return "Algo ha ido mal en el chequeo. no podemos arrancar"

        else:
            return "El coche esta parado."
    
    def estado(self):
        print(f"El coche tiene {self.__ruedas} ruedas, un ancho {self.__anchoChasis}, y un largo de {self.__largo_chasis}.")

    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False


print(" A continuacuion creamos el primer objeto ".center(130, '-'))

miCoche=Coche() #Primera Instanciacion o instancia de clase
print(miCoche.arrancar(True))
miCoche.estado()

#A continuacuion creamos el segundo objeto
print(" A continuacuion creamos el segundo objeto ".center(130, '-'))

miCoche2=Coche() #Segunda Instanciacion o instancia de clase
print(miCoche2.arrancar(False))
miCoche2.estado()

