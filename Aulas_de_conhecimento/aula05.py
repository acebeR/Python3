"""
input
"""
nome = input('Digite seu nome: ')
print('Resposta: ', nome)


"""
if else
"""

entrada = input('Voce quer "Entrar" ou "Sair" ?')
print('Resposta: ', entrada)

if entrada == 'entrar':
    print('Voce entrou!')
elif entrada == 'sair': 
    print('Voce saiu!')
else:
    print('Opcao errada!')

"""
Operadores
"""

maior = 2>1
print(maior)
maior_ou_igual = 2>=2
print(maior_ou_igual)
menor = 1< 2
print(menor)
menor_ou_igual = 2 <= 2
print(menor_ou_igual)
igual = 'a' == 'a'
print(igual)
diferente = 'a' != 'a'
print(diferente)

