class Galleta:
    sabor = "dulce"
    chocolate = False
    
    def __init__(self, sabor, chocolate):
        self.sabor = sabor
        self.chocolate = chocolate
        print("Soy una galletita recien horneadita")


    def chocolatear(self):
        self.chocolate = True

galleta = Galleta("salada", True)
print(galleta.sabor)
print(galleta.chocolate)

