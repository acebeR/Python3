# Exercício - sistema de perguntas e respostas
perguntas = [
    {
        'Pergunta': 'Quanto e 2+2?',
        'Opcoes': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto e 5*5?',
        'Opcoes': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto e 10/2?',
        'Opcoes': ['4', '5', '2', '1'],
        'Resposta': '5',
    }
]

def percorrerOpcoes(opcoes):
    i = 65
    for op in opcoes:
        print(chr(i) , ") " , op)
        i+= 1

def verifica_resposta(respostaEntrada,respostaIndice):
    indice = transdormaLetraIndice(respostaEntrada.upper())
    if indice == respostaIndice:
        return True
    return False

    

def transdormaLetraIndice(respostaEntrada):
    if respostaEntrada == 'A':
        return 0
    if respostaEntrada == 'B':
        return 1
    if respostaEntrada == 'C':
        return 2
    if respostaEntrada == 'D':
        return 3
    if respostaEntrada == 'E':
        return 4
    return -1

def descobreIndiceResposta(lista,resposta):
    i = 0
    for obj in lista:
        if obj == resposta:
            return i
        i += 1

def mensagemRetorno(msgCerto,msgErrado,resposta,respostaObj):
    msgretorno = ""
    if resposta:
        msgretorno += f"{msgCerto}\nResposta: {respostaObj}"
    else:
        msgretorno += f"{msgErrado}\nResposta: {respostaObj}"
    
    return msgretorno

def init():
    for pergunta in perguntas:
        opcoes = pergunta.get('Opcoes')
        print(pergunta.get('Pergunta'))
        percorrerOpcoes(opcoes)
        respostaEntrada = input('Qual e a letra correspondente para a resposta correta? Letra:  ')
        respostaCorreta = verifica_resposta(respostaEntrada,descobreIndiceResposta(opcoes, pergunta.get('Resposta')))
        
        print("**************************************************")
        print(mensagemRetorno("Parabens!! Esta resposta esta correta.","Deixa para a proxima! Esta resposta esta errada.", respostaCorreta, pergunta.get('Resposta')))
        print("**************************************************")
        
init()
