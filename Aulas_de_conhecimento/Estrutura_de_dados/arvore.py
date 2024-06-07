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
    root = No(3)
    root.esquerda = No(2)
    root.direita = No(13)
    root.direita.esquerda = No(7)
    root.direita.direita = No(17)
    root.direita.esquerda.direita = No(9)
    root.direita.direita.direita = No(23)
    root.direita.direita.direita.esquerda = No(21)
    root.direita.direita.direita.direita = No(25)


    print("Atravessa em pre-ordem > ")
    preOrdemNo(root)
    print(arvorePre)
    print("Atravessa Em-ordem > ")
    EmOrdemNo(root)
    print(arvoreEm)
    print("Atravessa Pos-ordem > ")
    PosOrdem(root)
    print(arvorePos)

