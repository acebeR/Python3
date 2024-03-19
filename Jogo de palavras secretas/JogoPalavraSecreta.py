"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import geradorPalavras 
import os

# Funcao
def populaPlaca(letra,placa,posicao):
    placa[posicao] = letra
    return placa
def imprimePlaca(placa):
    limpar_terminal()
    print('Palavra: ',placa)
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#Variaveis
palavra = 'Teste'
i = 0
j = 0
resposta = 'n'
contador = 0
placa = []
tamanho_palavra = 0
fracasso = 0
qtd = 0
placa_letras_erradas = []

palavra = geradorPalavras.get_random_word()
tamanho_palavra = len(palavra)
# Popular placa
while j < tamanho_palavra:
    placa.append('_')
    j += 1

print('---- Tente acertar a Palavra ------')
imprimePlaca(placa)
print('----------')

# Logica 
while resposta != 's':
    i = 0
    fracasso = 0
    imprimePlaca(placa)
    print('Letras erradas: ', placa_letras_erradas)
    letra_da_vez = input('Digite uma letra: ')
    qtd += 1 
    
    while i < tamanho_palavra:
        if letra_da_vez.lower() == palavra[i].lower():
            contador += 1
            placa = populaPlaca(letra_da_vez, placa,i)
            imprimePlaca(placa)
        else:
            fracasso += 1
        i += 1
        if contador == tamanho_palavra:
           print(' ')
           print('****************************')
           print('Parabens!!!') 
           print('Quantidade de tentativas: ', qtd)
           print('****************************')
           resposta = 's'
           break
    if fracasso == tamanho_palavra:
        print('Esta letra não possui na palavra!')
        placa_letras_erradas.append(letra_da_vez)
    if contador != tamanho_palavra:
        resposta = input('Deseja PARAR de tentar? (s) para sim.')
        limpar_terminal()
if resposta == 's' and contador != tamanho_palavra:
        print(' ')
        print('*********************************')
        print('Que pena, voce desistiu muito rápido...') 
        print('Quantidade de tentativas: ', qtd)
        print('A palavra era: ', palavra)
        print('*********************************')





