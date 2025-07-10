# Classe base
from abc import ABC, abstractmethod
class Conta:
    def __init__(self, numero,agencia,saldo):
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo


    def depositar(self):
        valor = input("Digite o valor que deseja adicionar na conta: ")
        saldo = saldo + valor

    @abstractmethod
    def sacar(self, valor):
        pass

class ContaCorrente(Conta):
    def tipo(self):
        return "Conta Corrente"
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para saque.")

class ContaPoupanca(Conta):
    def tipo(self):
        return "Conta Poupança"
    
    def sacar(self, valor):
        taxa = 0.02 * valor  
        total = valor + taxa
        if total <= self.saldo:
            self.saldo -= total
            print(f"Saque de R${valor:.2f} (+R${taxa:.2f} taxa). Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para saque.")

