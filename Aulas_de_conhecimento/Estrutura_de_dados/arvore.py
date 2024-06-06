# Estrutura de dados Arvore pré-ordem
arvorePre = []
arvoreEm = []
arvorePos = []

class No:
    def __init__(raiz,valor):
        raiz.valor = valor
        raiz.esquerda = None
        raiz.direita = None

def preOrdemNo(no):
    if no is None:
        return
    
    #visita o no
    arvorePre.append(no.valor)
    #percorre a esquerda
    preOrdemNo(no.esquerda)
    #percorre a direita
    preOrdemNo(no.direita)

def EmOrdemNo(no):
    if no is None:
        return
    
    #percorre a esquerda
    EmOrdemNo(no.esquerda)
    #visita o no
    arvoreEm.append(no.valor)
    #percorre a direita
    EmOrdemNo(no.direita)

def PosOrdem(no):
    if no is None:
        return
    
    #percorre a esquerda
    PosOrdem(no.esquerda)
    #percorre a direita
    PosOrdem(no.direita)
    #visita o no
    arvorePos.append(no.valor)


if __name__ == "__main__":
    root = No('A')
    root.esquerda = No('B')
    root.direita = No('C')
    root.esquerda.esquerda = No('D')
    root.esquerda.direita = No('E')
    root.direita.direita = No('F')

    print("Atravessa em pre-ordem > ")
    preOrdemNo(root)
    print(arvorePre)
    print("Atravessa Em-ordem > ")
    EmOrdemNo(root)
    print(arvoreEm)
    print("Atravessa Pos-ordem > ")
    PosOrdem(root)
    print(arvorePos)

