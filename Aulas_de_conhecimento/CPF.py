# print('ternario')
# condicao = 10 == 10
# variavel = 'valor' if condicao else 'Outro valor' 
# print(variavel)

# Exercicio
"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# Funcao
def retirarNumerosLista(lista,posicao_numero_del):
    i = 0
    resposta = []

    for item in lista:
        if i != posicao_numero_del:
            resposta.append(item)
        i += 1

    return resposta
  
def eNumero(value):
    try:
        float(value)
    except ValueError:
        return False
    return True

def retiraCaracter(lista):
    resp = []
    for item in lista:
        if eNumero(item) == True :
            resp.append(item)
    return resp

def multiplicaNumero(numero, index):
    return eval(numero)*index

def passo1(lista,numMultInit):
    i = numMultInit
    listaMult = []
    mult = 0
    for item in lista:
        mult = multiplicaNumero(item,i)
        listaMult.append(mult)
        i -= 1
    return listaMult

def passo2(lista):
    soma = 0
    for item in lista:
        soma = soma + item
    return soma

def passo3(somatorio):
    return somatorio * 10

def passo4(mult):
    rsp = mult % 11
    if rsp > 9:
        return 0
    else: return rsp

def valida(cpfGerado, cpfFornecido):
    if cpfGerado == cpfFornecido:
        return True
    else: return False

# Init
cpf = '746.824.890-70'
cpfNumeros = retiraCaracter(cpf)
# Primeiro digito depois do -
cpfSemDoisUltimos = retirarNumerosLista(cpfNumeros,10)
cpfSemDoisUltimos = retirarNumerosLista(cpfSemDoisUltimos,9)
p1 = passo1(cpfSemDoisUltimos,10)
p2 = passo2(p1)
p3 = passo3(p2)
p4Dois = passo4(p3)
print(p4Dois)
# Segundo digito depois do -
cpfSemUmUltimo = retirarNumerosLista(cpfNumeros,10)
p1 = passo1(cpfSemUmUltimo,11)
p2 = passo2(p1)
p3 = passo3(p2)
p4Um = passo4(p3)
print(p4Um)

stringGerado = ''.join(cpfSemDoisUltimos)
stringFornecido = ''.join(cpfNumeros)
novo_cpf = f'{stringGerado}{p4Dois}{p4Um}'
print(stringFornecido,'-',novo_cpf)
resposta = valida(novo_cpf,stringFornecido)
print('CPF valido: ',resposta)