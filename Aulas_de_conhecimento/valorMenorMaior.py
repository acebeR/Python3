"""
Exercicio: O usuario vai digitar dois valores e o programa tem que imprimir o valor 
maior primeiro depois o menor 
"""

print('--------Valor maior --------')
valor_1 = input('Digite o valor 1: ')
valor_2 = input('Digite o valor 2: ')

if valor_1 == valor_2:
    print('Os valores são iguais: ', valor_1,' = ',valor_2)    
elif valor_1 > valor_2:
    print('Valor: ', valor_1,' > ',valor_2)
else:
    print('Valor: ', valor_2,' > ',valor_1)
print('-------- Fim --------')

