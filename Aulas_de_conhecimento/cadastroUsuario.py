"""
Pedir ao usuario:  o nome, idade.
    Se os dois forem digitados, mostre:
    Seu nome {}
    Seu nome invertido {}
    Se o nome contem ou nao, espacos
    A primeira letra do nome 
    A ultima letra do nome
Se nada for digitado coloque uma mensagem.
"""

print('----- Bem vindo -----')
nome = input('Por favor, digite seu nome: ')
idade = input('Por favor, digite sua idade: ')
print('----- Suas Informações -----')
if nome.strip() != "" and idade.strip() != "":
    print(f'Seu nome: {nome}')
    print(f'Seu nome invertido: {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contem espacos!')
    if ' ' not in nome:
        print(f'Seu nome nao contem espacos!')
    print(f'Sua primeira letra do nome: {nome[0]}')
    print(f'Sua ultima letra do nome: {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios!')