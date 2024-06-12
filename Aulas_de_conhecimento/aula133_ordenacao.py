# Ordenaçao
lista = [{'nome':'Rebeca'},{'nome':'Leandro'},{'nome':'Ana'}]

# Ordena direto na lista
# l1 = lista
# l1.sort(key=lambda item: item['nome'])

l2 = sorted(lista,key=lambda item: item['nome'])

# Imprimir
print('Original: ',lista)
# print('L1: ',l1)
print('L2: ',l2)