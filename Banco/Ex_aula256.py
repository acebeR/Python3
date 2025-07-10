# Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
# Criar um sistema bancário (extremamente simples) que tem clientes, contas e
# um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
# possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

# Conta (ABC)
#     ContaCorrente
#     ContaPoupanca

# Pessoa (ABC)
#     Cliente
#         Clente -> Conta

# Banco
#     Banco -> Cliente
#     Banco -> Conta

# Dicas:
# Criar classe Cliente que herda da classe Pessoa (Herança)
#     Pessoa tem nome e idade (com getters)
#     Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
# Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
#     ContaCorrente deve ter um limite extra
#     Contas têm agência, número da conta e saldo
#     Contas devem ter método para depósito
#     Conta (super classe) deve ter o método sacar abstrato (Abstração e
#     polimorfismo - as subclasses que implementam o método sacar)
# Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
# Banco será responsável autenticar o cliente e as contas da seguinte maneira:
#     Banco tem contas e clentes (Agregação)
#     * Checar se a agência é daquele banco
#     * Checar se o cliente é daquele banco
#     * Checar se a conta é daquele banco
# Só será possível sacar se passar na autenticação do banco (descrita acima)
# Banco autentica por um método.
from Banco import Banco
from Cliente import Cliente
from Conta import ContaCorrente, ContaPoupanca

bancos = []
def menu():    
    resposta = 's'
    while resposta == 's':
        primeiroPasso = 0
        while primeiroPasso != 1 and primeiroPasso != 2:
            print("---- Bem vindo ao central de Bancos ----\n")
            listarBancos()
            print("-----------")
            print("O que deseja fazer:\n")
            print("1 - Cadastrar um banco\n")
            print("2 - Entrar em um banco\n")
            try:
                primeiroPasso = int(input("Opção: "))
                if primeiroPasso == 1:
                    banco_bb = cadastraBanco()
                    bancos.append(banco_bb)
                else:
                    print("em construcao")
            except ValueError:
                print("Digite um número válido.")
        resposta = input("Deseja continuar pesquisando? (s)Sim: ")

def menu2():
    resposta = 0
    while resposta > 0 and resposta < 7:
        print("1 - Cadastrar Conta")
        print("2 - Listar Contas")
        print("3 - Cadastrar Cliente")
        print("4 - Listar Clientes")
        print("5 - Vincular cliente conta")
        print("6 - Lista cliente e conta")
        resposta = input("Escolha uma opção: ")
    match resposta:
        case 1:
            conta1 = ContaCorrente(1001, 12345, 1000, limite=300)
        case 2:
            print("Listar")
        case 3:
            cliente1 = Cliente("João", 30)
        case 4:
            print("Sair")
        case 5:
            cliente1.inserir_conta(conta1)
        case 6:
            print("Sair")
        case _:
            print("Opção inválida")
def logarBanco():
    idBanco = int(input("Em qual banco deseja entrar (id)?"))
    valida = False
    for banco in bancos:
        if banco.id == idBanco:
            valida = True
            break
    if valida:
        menu2()

    else:
        "Este Banco não está cadastrado"


def listarBancos():
    if bancos:
        for banco in bancos:
            print(f"Banco: {banco.id} - Agências: {banco.agencias}")
    else:
        print("Ainda não possui bancos cadastrados!")

def cadastraBanco():
    qtdagencias = int(input("Quantas agencias quer cadastra no seu banco?"))
    agencias = []
    id = 0
    while qtdagencias > 0:
        agencias.append(int(input(f"Agência {qtdagencias}: ")))
        qtdagencias = qtdagencias - 1
    if bancos:
        id = len(bancos)
    else:
        id = 1;        

    return Banco(id,agencias)
    

def main():
    menu()


if __name__ == "__main__":
    main()
