class Coche:
    """Abstraccion de los objetos coche."""
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print("Hay", gasolina, "litros")
        
    def arrancar(self, valor):
        if self.gasolina > 0:
            print("Arranca")
        else:
            print("No Arranca")
                    
    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print("Quedan", self.gasolina, "litros")
        else:
            print("No se mueve")