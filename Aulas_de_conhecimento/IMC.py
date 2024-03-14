"""
Exercicio: Impimir Nome tem tantos de altura, pesa tantos quilos e seu IMC [e]
"""

#Variaveis
nome = 'Rebeca'
altura = 1.68
peso = 61
imc = peso / ( altura ** 2 )

linha_1 = f'{nome} tem {altura:.2f} de altura, '
linha_2 = f'pesa {peso} quilos e seu imc e {imc}'
print(linha_1, linha_2)

# Outra forma de formatar
string ='Nome={} Altura={} Peso={} IMC={}'
formato = string.format(nome,altura,peso,imc)
print(formato)