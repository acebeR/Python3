frase = 'Você atingirá o sucesso quando apresentar '\
'com orgulho as cicatrizes que adquiriu ao longo da sua jornada.'
# frase = 'rebeca r b e'

letras_ordenadas = ''.join(sorted(frase))
print(letras_ordenadas)

resposta = []
letras_processadas = []

# Iterar sobre a string ordenada
for i in range(len(letras_ordenadas)):
    # Ignorar espaços em branco
    if letras_ordenadas[i] == ' ':
        continue
    
    letra = letras_ordenadas[i]
    
    # Verificar se a letra já foi processada
    if letra in letras_processadas:
        continue

    qtd = letras_ordenadas.count(letra)
    
    # Criar um novo objeto e adicionar à resposta
    objeto_da_vez = {'letra': letra, 'qtd': qtd}
    resposta.append(objeto_da_vez)

    # Adicionar a letra à lista de letras processadas
    letras_processadas.append(letra)

print(resposta)