"""
Interando Strings
"""
print('----- Bem vindo -----')
palavra = input('Digite qualquer palavra: ')

i = 0
letra = ''
palavra_com_asterisco = ''
while i < len(palavra):
    letra = palavra[i]
    print(f'A letra: "{letra}" está na posição {i}')
    palavra_com_asterisco += '*' + letra
    i += 1
print('A palavra digitada com asterisco é: ', palavra_com_asterisco)
print('----------------------------------')
# Ao contrário
i = len(palavra) - 1
letra = ''
palavra_ao_contrario = ''
while i >= 0:
    letra = palavra[i]
    print(f'A letra: "{letra}" está na posição {i}')
    palavra_ao_contrario += letra
    i -= 1
print('A palavra digitada ao contrário é: ', palavra_ao_contrario)
print('----------------------------------')
