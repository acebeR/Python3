class Caneta:
    def __init__(self,cor):
        # Quando coloca o _ é um acordo de todos que isso é privado.
        self._cor = cor

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self,valor):
        self._cor = valor

caneta = Caneta('Rosa')
print(caneta.cor)