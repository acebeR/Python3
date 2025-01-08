# Métodos de classes + factories
class Pessoa:
    ano = 2023
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    @classmethod
    def metodo_de_classe(cls):
        print("olooo")
                @classmethod
    def criar_com_50_anos(cls,nome):
        print(nome,50)

p1 = Pessoa('João', 34)
print(Pessoa.ano)
Pessoa.metodo_de_classe()

        