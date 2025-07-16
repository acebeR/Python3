# Classe base
from abc import ABC, abstractmethod
class Conta:
    def __init__(self, numero,agencia,saldo):
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo

    def to_dict(self):
        return {
            "numero": self.numero,
            "agencia": self.agencia,
            "saldo": self.saldo,
            "tipo": self.tipo()  # opcional: identifica o tipo no JSON
        }

    def depositar(self):
        try:
            valor = float(input("Digite o valor que deseja adicionar na conta: "))
            if valor <= 0:
                print("Valor deve ser positivo.")
                return
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    @abstractmethod
    def sacar(self, valor):
        pass

class ContaCorrente(Conta):
    def tipo(self):
        return "Conta Corrente"
    
    @classmethod
    def from_dict(cls, dados):
        return cls(dados["numero"], dados["agencia"], dados["saldo"])
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para saque.")

class ContaPoupanca(Conta):
    def tipo(self):
        return "Conta Poupança"
    
    @classmethod
    def from_dict(cls, dados):
        return cls(
            numero=dados["numero"],
            agencia=dados["agencia"],
            saldo=dados["saldo"]
        )
    
    def sacar(self, valor):
        taxa = 0.02 * valor  
        total = valor + taxa
        if total <= self.saldo:
            self.saldo -= total
            print(f"Saque de R${valor:.2f} (+R${taxa:.2f} taxa). Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para saque.")

