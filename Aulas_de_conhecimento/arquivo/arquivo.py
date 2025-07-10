class Arquivo:
    def __init__(self, nome):
        self.nome = nome
        self.linhas = []

    def getLinha(self):
        return len(self.linhas)

    def getNome(self):
        return self.nome

    def getQtdPalavras(self):
        qtdPalavras = 0
        for linha in self.linhas:
            qtdPalavras += len(linha.texto.split())
        return qtdPalavras
    
    def imprimeLinhas(self):
        for linha in self.linhas:
            print(linha.texto)

    

                        
        
