from Pessoa import Pessoa
class Cliente(Pessoa):
    def __init__(self, nome, idade, conta, id):
        super().__init__(nome, idade)
        self.id = id
        self.conta = conta

    def to_dict(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "id": self.id,
            "conta": self.conta.to_dict() if hasattr(self.conta, "to_dict") else self.conta
        }
    
    def mostrar_conta(self):
        print(f"Id: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Número: {self.conta.numero}")