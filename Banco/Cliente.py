from Pessoa import Pessoa
class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = conta

    def mostrar_conta(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Número: {self.conta.numero}")