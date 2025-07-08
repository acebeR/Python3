# Classe base
class Animal:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar(self):
        print(f"{self.nome} ataca de forma genérica.")

    def tomar_dano(self, dano):
        self.vida -= dano
        print(f"{self.nome} tomou {dano} de dano. Vida restante: {self.vida}")

class Leao(Animal):
    def atacar(self):
        print(f"{self.nome} dá uma patada feroz!")
        return 20

class Cobra(Animal):
    def atacar(self):
        print(f"{self.nome} dá uma mordida venenosa!")
        return 15

class Aguia(Animal):
    def atacar(self):
        print(f"{self.nome} mergulha do céu com as garras!")
        return 18
