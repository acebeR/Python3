# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


resposta = multiplica(1,2,10,8)
print(resposta)