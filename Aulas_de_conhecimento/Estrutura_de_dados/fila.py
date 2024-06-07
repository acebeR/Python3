class Fila:
    def __init__(ponteiro):
        ponteiro.itens = []
    def enfileirar(ponteiro,valor):
        ponteiro.itens.append(valor)
    def desenfileirar(ponteiro):
        ponteiro.itens.pop(0)
    

def init():
    fila = Fila()
    fila.enfileirar(10)
    fila.enfileirar(1)
    fila.enfileirar(5)
    fila.enfileirar(20)
    fila.desenfileirar()
    fila.desenfileirar()
    print(fila.itens)

init()

