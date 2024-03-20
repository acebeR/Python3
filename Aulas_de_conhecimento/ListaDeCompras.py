import os

#Variáveis
lista_compras = []
resposta = []
sair = 1

# Funcao
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
def inicio():
    limpar_terminal()
    print(" -------- Bem Vindo --------- ")
    print(" Este programa permite você adicionar, excluir ou editar seu item da lista de compras.")
    print(" ---------------------------- ")
def inserir():
    lista = []
    item = input('Digite o item(TEXTO) desejado: ')
    lista.append(item)
    return lista
def deletar(lista_entrada):
    item = input('Digite o item(TEXTO) desejado para deletar: ')
    lista_entrada.remove(item)
    return lista_entrada
def editar(lista_entrada):
    item = input('Digite o item(TEXTO) da lista desejado para editar: ')
    item_editado = input('Digite o novo item(TEXTO) para editar: ')
    index = lista_entrada.index(item)
    lista_entrada[index] = item_editado
    return lista_entrada
def listar(lista_entrada):
    i = 0
    print('***** Sua Lista ******')
    for item in lista_entrada:
        i +=1
        print(i, ' - ',item)
    print('**********************')


while sair == 1:
    inicio()
    listar(lista_compras)
    print("Digite [i]Inserir, [d]deletar, [e]Editar")
    resposta = input('Opção: ')
    if resposta.lower() == 'i':
        lista_compras += inserir()
    elif resposta.lower() == 'd':
        lista_compras = deletar(lista_compras)
    elif resposta.lower() == 'e':
        lista_compras = editar(lista_compras)
    else:
        print('Esta opção não é valida!')
        input('')
