"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
resposta = 's'
par_impar = ''
while resposta == 's' or resposta == 'S':
    try:
        print('---- Primeiro programa ---')
        numero_inteiro = int(input('Digite um número inteiro para saber se é par ou impar: '))
        # Par ou ímpar
        if numero_inteiro % 2 == 0:
            par_impar = 'Par'
        else:
            par_impar = 'Ímpar'

        print(f'O número digitado é: {par_impar}')
    except ValueError: 
        print('O número digitado não é um inteiro!')

    print('------------------')
    resposta = input('Gostaria de tentar novamente? Digite "S" para sim:  ')
print('Obrigada...')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
resposta = 's'
horario = ''
hora = 0
while resposta == 's' or resposta == 'S':
    try:
        print('---- Segundo programa ---')
        print('Digite o horário de agora, siga o padrão 00:00.')
        horario = input('Digite aqui: ')
        # Nao deixar padrao diferente passar
        print('******************************')
        if ':' in horario:
            hora = int(horario[0:2])
            if hora >= 0 and hora <= 11:
                print(f'Bom Dia, agora são: {horario}')
            elif hora >= 12 and hora <= 17:
                print(f'Boa Tarde, agora são: {horario}')
            else:
                print(f'Boa Noite, agora são: {horario}')
        else:
            print('O padrao está incorreto! Siga o padrão 00:00!')
        print('**************************') 
    except ValueError: 
        print('Não foi possível transformar texto em inteiro!')

    print('------------------')
    resposta = input('Gostaria de tentar novamente? Digite "S" para sim:  ')
print('Obrigada...')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

resposta = 's'
primeiro_nome = ''
while resposta == 's' or resposta == 'S':
    try:
        print('---- Terceiro programa ---')
        primeiro_nome = input('Digite o seu primeiro nome: ')
        # Nao deixar mais de um passsar
        print('******************************')
        if ' ' not in primeiro_nome:
            if len(primeiro_nome) <= 4:
                print('Seu nome é curto!')
            elif len(primeiro_nome) == 5 or len(primeiro_nome) == 6:
                print('Seu nome é normal!')
            else:
                print('Seu nome é muito grande!')
        else:
            print('Houve mais que o primeiro nome digitado!')
    except ValueError: 
        print('Não foi possível transformar texto em inteiro!')

    print('------------------')
    resposta = input('Gostaria de tentar novamente? Digite "S" para sim:  ')
print('Obrigada...')