# Herança é uma forma de criar uma nova classe 
# (chamada de classe filha ou subclasse) baseada em uma classe existente 
# (chamada de classe pai ou superclasse). A classe filha herda todos os 
# atributos e métodos da classe pai, podendo, se necessário, modificar ou 
# adicionar novos atributos ou métodos.

# Classe Pai (Superclasse)
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def falar(self):
        raise NotImplementedError("O método 'falar' precisa ser implementado")

# Classe Filha (Subclasse)
class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)  
        self.raca = raca
    
    def falar(self):
        return f"{self.nome} diz: Au au!"

# Classe Filha (Subclasse)
class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome) 
        self.cor = cor
    
    def falar(self):
        return f"{self.nome} diz: Miau!"


cachorro = Cachorro("Rex", "Labrador")
gato = Gato("Mimi", "Preto")


print(cachorro.falar())  
print(gato.falar())  
