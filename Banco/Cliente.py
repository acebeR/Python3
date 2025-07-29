from Pessoa import Pessoa
class Cliente(Pessoa):
    def __init__(self, nome, idade, idconta, id):
        super().__init__(nome, idade)
        self.id = id
        self.idconta = idconta

    def to_dict(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "id": self.id,
            "conta": self.idconta
        }
    
    def mostrar_conta(self):
        print(f"Id: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Número: {self.idconta}")