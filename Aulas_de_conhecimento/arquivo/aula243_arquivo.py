# Ler um arquivo .txt e mostrar:
# Quantas linhas ele tem
# Quantas palavras no total
# Quantas vezes uma palavra específica aparece
# As 5 palavras mais frequentes (opcional/desafio extra)
from contextlib import contextmanager
import arquivo
import linha

# Instância da classe Arquivo
objArquivo = arquivo.Arquivo("")

def mescla():
    lista = []
    for linha in objArquivo.linhas:
        texto_linha = linha.texto.split()
        for palavra in texto_linha:
            lista.append(palavra)
    return lista

def listaPalavrasRepetidas():
    retorno = []
    lista = mescla()
    for i, palavra1 in enumerate(lista):
        for j, palavra2 in enumerate(lista):
            if palavra1 == palavra2 and i != j:
                if palavra1 not in retorno:
                    retorno.append(palavra1)
    return retorno
def qtdVezesPalavraEspecificaAparece(palavra):
    soma = 0
    lista = mescla()
    for palavra1 in lista:
        if palavra == palavra1:
            soma = soma + 1
    return soma

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivoOpen = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivoOpen
    except Exception as e:
        print('Ocorreu erro:', e)
    finally:
        print('Fechando arquivo')
        arquivoOpen.close()
        print("====================")
        print("Nome do Arquivo: ", objArquivo.getNome())
        print("Quantidade de linhas: ", objArquivo.getLinha())
        print("Quantidade de palavras: ", objArquivo.getQtdPalavras())
        repetidas = listaPalavrasRepetidas()
        print("Quantidade de palavras repetidas: ", len(repetidas))
        for palavra in repetidas:
            print("Quantidade de vezes que a palavra ", palavra, " foi repetida: ", qtdVezesPalavraEspecificaAparece(palavra))
        print("====================")
        

with my_open('entrada.txt', 'r') as arquivo:
    objArquivo.nome = "entrada.txt"
    qtdLinha = 0

    for texto_linha in arquivo:
        texto_linha = texto_linha.strip()  
        if texto_linha:
            qtdLinha += 1
            palavras = texto_linha.split()
            
            linha_obj = linha.Linha(qtdLinha, texto_linha,len(palavras))
            objArquivo.linhas.append(linha_obj)
    # objArquivo.qtdPalavras = qtdPalavras
