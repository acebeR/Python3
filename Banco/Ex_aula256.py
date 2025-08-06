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
from banco_arquivo import Banco, salvar_banco_em_arquivo,carregar_banco_por_id, salvar_cliente_no_banco, listar_clientes_do_banco,salvar_contas_do_banco,listar_contas_do_banco, listar_conta_por_id,depositar_em_conta,atualizar_conta_no_banco
import json
import os
import datetime

def menu():    
    primeiroPasso = 0
    while primeiroPasso != 1 and primeiroPasso != 2:
        limpar_console()
        print("---- Bem vindo ao central de Bancos ----\n")
        imprimeBancos(0)
        print("-----------")
        print("O que deseja fazer:\n")
        print("1 - Cadastrar um banco\n")
        print("2 - Entrar em um banco\n")
        print("3 - Sair do Programa\n")
        try:
            primeiroPasso = int(input("Opção: "))
            if primeiroPasso == 1:
                banco_bb = cadastraBanco()
                salvar_banco_em_arquivo(banco_bb, "db_banco.json")
            else:
                if primeiroPasso == 3:
                    break
                else:
                    logarBanco()
        except ValueError:
            print("Digite um número válido.")
        if primeiroPasso == 3:
            return

def menu2(banco):
    limpar_console()
    listarBancos(banco.id)
    print("Deseja mexer com:")
    resposta = 0
    while resposta == 0 or resposta != 1 or resposta != 2 or resposta != 3:
        print("1 - Cliente")
        print("2 - Conta")
        print("3 - Voltar para o menu inicial\n")
        resposta = int(input("Escolha uma opção: "))

        match resposta:
            case 1:
                menucliente(banco)
            case 2:
                menuConta(banco)
            case 3:
                menu()
            case _:
                print("Opção inválida!\n")


def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# ---------------- Banco
def logarBanco():
    idBanco = int(input("Em qual banco deseja entrar (id)? "))
    bancos_raw = listarBancos(0)  # Supondo que retorna lista de dicts ou objetos misturados

    bancoEncontrado = None
    for banco in bancos_raw:
        # Se 'banco' for dict, converta para objeto Banco
        if isinstance(banco, dict):
            # Converter para Banco objeto usando from_dict
            banco_obj = Banco.from_dict(banco)
        else:
            banco_obj = banco

        if banco_obj.id == idBanco:
            bancoEncontrado = banco_obj
            break

    if bancoEncontrado:
        limpar_console()
        print("================")
        print("Você está no banco ")
        imprimeBancos(bancoEncontrado.id)
        menu2(bancoEncontrado)
    else:
        print("Este Banco não está cadastrado")

def listarBancos(identrada):
    bancos = carregar_banco_por_id("db_banco.json")
    if identrada == 0:
        return bancos
    else:
        for banco in bancos:
            if banco.id == identrada:
                return banco
            
def imprimeBancos(identrada):
    bancos = listarBancos(identrada)
    if identrada == 0:
        for banco in bancos:
            print("Banco: ", banco.id," - Agencia: ", banco.agencias)
    else:  
        if type(bancos) == list:
            for banco in bancos:
                if banco.id == identrada:
                    print("Banco: ", banco.id," - Agencia: ", banco.agencias)
        else:
            print("Banco: ", bancos.id," - Agencia: ", bancos.agencias)

def cadastraBanco():
    data = datetime.datetime.now()
    data_formatada = data.strftime("%d-%m-%Y %H:%M")
    bancos = listarBancos(0)
    qtdagencias = int(input("Quantas agencias quer cadastra no seu banco? "))
    agencias = []
    id = 0
    while qtdagencias > 0:
        agencias.append(int(input(f"Agência {qtdagencias}: ")))
        qtdagencias = qtdagencias - 1
    if bancos:
        id = len(bancos) + 1
    else:
        id = 1;        

    return Banco(id,agencias,data_formatada)
    
# ---------------- Conta
def imprimeContas(idBanco, identrada):
    print(f"Banco ID: {idBanco}")
    contas = listar_contas_do_banco(idBanco, "db_banco.json")

    if not contas:
        return

    if identrada == 0:
        for conta in contas:
            print("Conta:", conta["numero"], "- Agência:", conta["agencia"])
    else:
        encontrou = False
        for conta in contas:
            if conta["numero"] == identrada:
                print("Conta:", conta["numero"], "- Agência:", conta["agencia"])
                encontrou = True
                break
        if not encontrou:
            print(f"Conta {identrada} não encontrada no banco {idBanco}.")
def menuConta(banco):
    resposta = 0
    while resposta == 0 or resposta != 1 or resposta != 2 or resposta != 3 or resposta != 4:
        limpar_console()
        print("============ Menu Conta =============")
        print("1 - Cadastrar")
        print("2 - Depositar")
        print("3 - Alterar")
        print("4 - Voltar")
        resposta = int(input("Escolha uma opção: "))
        contas = listar_contas_do_banco(banco.id)
        print("======= Contas do Banco ", banco.id, " =======")
        imprimeContas(banco.id,0)
        print("=================")
        match resposta:
            case 1:
                respConta = 0
                agencia = 0
                while respConta < 1 or respConta > 2:
                    print("1 - Corrente")
                    print("2 - Poupança")
                    respConta = int(input("Qual o tipo de conta? "))

                while validaAgencia(banco.agencias,agencia) == False:
                    print("Agencias - ",banco.agencias)
                    agencia = input("Qual a agencia? ")
                id = 1
                data = datetime.datetime.now()
                data_formatada = data.strftime("%d-%m-%Y %H:%M")
                if contas:
                    id = len(contas) + 1
                if respConta == 1:
                    conta = ContaCorrente(id, agencia, 0, data_formatada)
                else:
                    conta = ContaPoupanca(id, agencia, 0, data_formatada)
                print("==============")
                print("Conta cadastrada com sucesso ", conta.numero)
                banco.adicionar_conta(conta)
                salvar_contas_do_banco(banco,"db_banco.json")
            case 2:
                print("======= Depósito =======")
                print("Contas:")
                imprimeContas(banco.id, 0)
                conta = int(input("Em qual conta deseja depositar? "))
                try:
                    valor = float(input("Valor desejado para depósito: "))
                except ValueError:
                    print("Valor inválido! Digite um número decimal válido.")
                    return  # ou trate o erro do jeito que preferir

                imprimeClientes(banco.id, 0)
                depositar_em_conta(banco, conta, valor, "db_banco.json")
            case 3: 
                respConta = 0
                while not conta:
                    respConta = int(input("Qual Conta deseja Alterar? "))
                    conta = findConta(contas,respConta)
                    resp1 = 'n'
                    while resp1 != 'n' or resp1 != 's':
                        resp1 = int(input("Deseja manter a conta do tipo: ", conta.tipo, "?"))
                    if resp1 == 'n':
                        resp = 0
                        while resp < 1 or resp > 2:
                            print("1 - Corrente")
                            print("2 - Poupança")
                            resp = int(input("Qual o tipo de conta? "))
                    else:
                        if "corrente" in conta.tipo.lower():
                            resp = 1
                        else:
                            resp = 2
                    valida = False
                    while valida == False:
                        print("Agencias - ", banco.listarAgencias)
                        agencia = input("Qual a agencia? ")
                        valida = validaAgencia(banco.agencias, agencia)
                    id = 1
                    if contas:
                        id = len(contas) + 1
                    if respConta == 1:
                        conta = ContaCorrente(id, agencia,0)
                    else:
                        conta = ContaPoupanca(id, agencia, 0)

                    atualizar_conta_no_banco(banco.id,conta)
            case 4:
                menu2(banco)
            case _:
                print("Opção inválida")

def findConta(contas,entrada):
    if entrada == 0:
        return {}
    for conta in contas:
        if int(conta) == int(entrada):
            return conta
    print("Conta inválida!\n")
    return {}

def validaAgencia(agencias,entrada):
    if entrada == 0:
        return False
    for agencia in agencias:
        print(int(agencia), int(entrada))
        if int(agencia) == int(entrada):
            return True
    # limpar_console()
    print("Agência inválida!\n")
    return False
# ---------------- Cliente
def imprimeClientes(idBanco,identrada):
    print(f"Banco ID: {idBanco}")
    clientes = listar_clientes_do_banco(idBanco, "db_banco.json")
    if identrada == 0:
        for cliente in clientes:
            print("Cliente: ", cliente["nome"]," - Idade: ", cliente["idade"])
    else:  
        if type(clientes) == list:
            for cliente in clientes:
                if cliente.id == identrada:
                    print("Cliente: ", cliente["nome"]," - Idade: ", cliente["idade"])
        else:
            print("Cliente: ", clientes["nome"]," - Idade: ", clientes["idade"])
def menucliente(banco):
    resposta = 0
    while resposta == 0 or resposta > 3:
        limpar_console()
        print("============ Menu Cliente =============")
        print("1 - Cadastrar")
        print("2 - Alterar")
        print("3 - Voltar")
        resposta = int(input("Escolha uma opção: "))

        clientes = listar_clientes_do_banco(banco.id)
        print("======= Todos os clientes do banco: ", banco.id, " =======")
        imprimeClientes(banco.id,0)
        print("===================================")
        match resposta:
            case 1:
                contas = listar_contas_do_banco(banco.id)
                if len(contas) > 0:
                    print("======= Cadastrar Cliente no banco: ", banco.id, " =======")
                    nome = input("Nome do cliente: ")
                    idade = int(input("Idade do cliente: "))
                    imprimeContas(banco.id,0)
                    idconta = int(input("Qual a conta? "))
                    conta = listar_conta_por_id(banco.id, idconta)
                    data = datetime.datetime.now()
                    data_formatada = data.strftime("%d-%m-%Y %H:%M")
                    id = 1
                    if clientes:
                        id = len(clientes) + 1
                    else:
                        id = 1
                    cliente = Cliente(nome, idade, conta,id,data_formatada)
                    salvar_cliente_no_banco(cliente,banco.id,"db_banco.json")
                else:
                    limpar_console()
                    print("Atenção: Cadastre uma conta para cadastrar um cliente!")
            case 2:
                print("Em construcao")
            case 3:
                menu2(banco)
            case _:
                print("Opção inválida")
               

def main():
    menu()


if __name__ == "__main__":
    main()
