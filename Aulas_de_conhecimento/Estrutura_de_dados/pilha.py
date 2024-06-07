class Pilha:
    def __init__(ponteiro):
        ponteiro.itens = []

    def esta_vazia(ponteiro):
        return len(ponteiro.itens) == 0

    def empilhar(ponteiro, item):
        ponteiro.itens.append(item)

    def desempilhar(ponteiro):
        if not ponteiro.esta_vazia():
            return ponteiro.itens.pop()
        else:
            raise IndexError("Desempilhar de uma pilha vazia")

    def topo(ponteiro):
        if not ponteiro.esta_vazia():
            return ponteiro.itens[-1]
        else:
            raise IndexError("Acessar o topo de uma pilha vazia")

    def tamanho(ponteiro):
        return len(ponteiro.itens)

    def __str__(ponteiro):
        return str(ponteiro.itens)


# Exemplo de uso
def init():
    pilha = Pilha()
    pilha.empilhar(1)
    pilha.empilhar(2)
    pilha.empilhar(3)
    print("Pilha:", pilha)
    print("Topo:", pilha.topo())
    print("Desempilhar:", pilha.desempilhar())
    print("Pilha após desempilhar:", pilha)
    print("Tamanho da pilha:", pilha.tamanho())

init()
