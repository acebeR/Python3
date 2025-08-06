import json
import os
from Banco import Banco
from Cliente import Cliente
from Conta import Conta
import datetime


import os
import json
import datetime

def salvar_banco_em_arquivo(banco, nome_arquivo):
    # Verifica se é uma instância de Banco
    if not isinstance(banco, Banco):
        raise TypeError("O objeto informado não é uma instância da classe Banco.")

    # Usa a data atual se banco.dataCadastro não estiver definido
    if hasattr(banco, 'dataCadastro') and banco.dataCadastro:
        data = banco.dataCadastro
        if isinstance(data, datetime.datetime):
            data_formatada = data.strftime("%d-%m-%Y %H:%M")
        elif isinstance(data, str):
            try:
                data_obj = datetime.datetime.strptime(data, "%d-%m-%Y %H:%M")
                data_formatada = data_obj.strftime("%d-%m-%Y %H:%M")
            except ValueError:
                data_formatada = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        else:
            data_formatada = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    else:
        data_formatada = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

    # Cria o dicionário para salvar
    dados_novos = {
        "id": banco.id,
        "agencias": banco.agencias,
        "clientes": banco.clientes,
        "contas": banco.contas,
        "dataCadastro": data_formatada
    }

    bancos = []

    # Carrega bancos existentes, se o arquivo existir
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            try:
                bancos = json.load(f)
            except json.JSONDecodeError:
                bancos = []

    # Atualiza banco existente ou adiciona novo
    atualizado = False
    for i, b in enumerate(bancos):
        if b['id'] == banco.id:
            bancos[i] = dados_novos
            atualizado = True
            break

    if not atualizado:
        bancos.append(dados_novos)

    # Salva novamente no arquivo
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(bancos, f, indent=4, ensure_ascii=False)

    print(f"Banco {banco.id} salvo com sucesso em '{nome_arquivo}'")


def carregar_banco_por_id(nome_arquivo):

    if not os.path.exists(nome_arquivo):
        return []

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

    bancos = []
    data = datetime.datetime.now()
    data_formatada = data.strftime("%d-%m-%Y %H:%M")
    for b in dados:
        banco = Banco(id=b.get('id'), dataCadastro=b.get('dataCadastro',data_formatada), agencias=b.get('agencias', []))
        banco.clientes = b.get('clientes', [])
        banco.contas = b.get('contas', [])
        bancos.append(banco)

    return bancos

def listar_clientes_do_banco(id_banco, nome_arquivo="db_banco.json"):
    """
    Retorna a lista de clientes do banco com o ID informado.

    Args:
        id_banco (int): ID do banco desejado.
        nome_arquivo (str): Nome do arquivo JSON.

    Returns:
        list: Lista de clientes do banco, ou lista vazia se não encontrado.
    """
    if not os.path.exists(nome_arquivo):
        return []

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            if not isinstance(dados, list):
                return []

            for banco in dados:
                if banco.get("id") == id_banco:
                    return banco.get("clientes", [])

    except (json.JSONDecodeError, FileNotFoundError):
        return []

    return []

def listar_contas_do_banco(id_banco, nome_arquivo="db_banco.json"):
    """
    Lista as contas do banco com o ID informado, lendo do arquivo JSON.

    Args:
        id_banco (int): ID do banco a ser buscado.
        nome_arquivo (str): Nome do arquivo JSON.

    Returns:
        list[dict]: Lista de contas (ou lista vazia se não houver ou não encontrar).
    """
    retorno = []
    if not os.path.exists(nome_arquivo):
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return []

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            bancos = json.load(f)
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")
        return []

    for banco in bancos:
        if banco.get("id") == id_banco:
            retorno = banco.get("contas", [])
            if retorno:
                return retorno

    print(f"Não foi encontrado contas no banco: {id_banco}.")
    return []
    
def salvar_contas_do_banco(banco, nome_arquivo="db_banco.json"):
    """
    Atualiza a lista de contas de um banco existente no arquivo db_banco.json.

    Args:
        banco (Banco): Objeto Banco contendo ID e contas (lista de objetos Conta).
        nome_arquivo (str): Caminho do arquivo JSON.
    """
    if not hasattr(banco, 'id') or not hasattr(banco, 'contas'):
        raise ValueError("Objeto banco inválido ou incompleto.")

    # Converte contas para dicionários
    contas_convertidas = [conta.to_dict() for conta in banco.contas]

    dados = []

    # Carrega o arquivo existente
    if os.path.exists(nome_arquivo):
        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Erro ao ler o arquivo JSON. Verifique se ele está corrompido.")
    else:
        raise FileNotFoundError(f"O arquivo '{nome_arquivo}' não foi encontrado.")

    # Atualiza as contas do banco com o ID correspondente
    banco_encontrado = False
    for i, registro in enumerate(dados):
        if registro.get("id") == banco.id:
            dados[i]["contas"] = contas_convertidas
            banco_encontrado = True
            break

    if not banco_encontrado:
        raise ValueError(f"Nenhum banco com ID {banco.id} encontrado no arquivo.")

    # Salva o arquivo atualizado
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    print(f"Contas do banco {banco.id} atualizadas com sucesso em {nome_arquivo}.")

def atualizar_conta_no_banco(id_banco, conta_atualizada, nome_arquivo="db_banco.json"):
    """
    Atualiza uma conta específica dentro de um banco no arquivo JSON.

    Args:
        id_banco (int): ID do banco onde a conta será atualizada.
        conta_atualizada (Conta): Objeto Conta com dados novos.
        nome_arquivo (str): Caminho para o arquivo JSON.
    """
    if not hasattr(conta_atualizada, 'numero') or not hasattr(conta_atualizada, 'to_dict'):
        raise ValueError("Objeto conta inválido ou incompleto.")

    if not os.path.exists(nome_arquivo):
        raise FileNotFoundError(f"Arquivo '{nome_arquivo}' não encontrado.")

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Erro ao ler o arquivo JSON. Verifique se está corrompido.")

    banco_encontrado = False
    conta_encontrada = False

    for banco in dados:
        if banco.get("id") == id_banco:
            banco_encontrado = True
            for i, conta in enumerate(banco.get("contas", [])):
                if conta.get("numero") == conta_atualizada.numero:
                    banco["contas"][i] = conta_atualizada.to_dict()
                    conta_encontrada = True
                    break
            break

    if not banco_encontrado:
        raise ValueError(f"Banco com ID {id_banco} não encontrado.")

    if not conta_encontrada:
        raise ValueError(f"Conta número {conta_atualizada.numero} não encontrada no banco {id_banco}.")

    # Salva os dados atualizados no JSON
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    print(f"Conta {conta_atualizada.numero} atualizada com sucesso no banco {id_banco}.")

def salvar_cliente_no_banco(cliente, id_banco, nome_arquivo="db_banco.json"):
    """
    Adiciona um único cliente ao banco com o ID informado e atualiza o arquivo JSON.

    Args:
        cliente: Cliente a ser adicionado (pode ser string, dict ou objeto serializável).
        id_banco (int): ID do banco onde o cliente será adicionado.
        nome_arquivo (str): Nome do arquivo onde os dados estão armazenados.
    """
    if not isinstance(id_banco, int):
        raise ValueError("ID do banco deve ser um número inteiro.")

    dados = []

    # Carrega os dados do arquivo
    if os.path.exists(nome_arquivo):
        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Erro ao ler o arquivo JSON. Verifique se ele está corrompido.")
    else:
        raise FileNotFoundError(f"O arquivo '{nome_arquivo}' não foi encontrado.")

    # Encontra o banco e adiciona o cliente
    banco_encontrado = False
    for banco in dados:
        if banco.get("id") == id_banco:
            if "clientes" not in banco or not isinstance(banco["clientes"], list):
                banco["clientes"] = []

            if isinstance(cliente, Cliente):
                banco["clientes"].append(cliente.to_dict())
            else:
                banco["clientes"].append(cliente)
            banco_encontrado = True
            break

    if not banco_encontrado:
        raise ValueError(f"Nenhum banco com ID {id_banco} encontrado no arquivo.")

    # Salva o arquivo novamente com o cliente adicionado
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    print(f"Cliente adicionado ao banco {id_banco} com sucesso.")




def listar_conta_por_id(id_banco, id_conta, nome_arquivo="db_banco.json"):
    """
    Retorna os dados de uma conta específica de um banco específico.

    Args:
        id_banco (int): ID do banco.
        id_conta (int): Número da conta.
        nome_arquivo (str): Caminho do arquivo JSON.

    Returns:
        dict | None: Dicionário com os dados da conta ou None se não encontrar.
    """
    if not os.path.exists(nome_arquivo):
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return None

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            bancos = json.load(f)
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON.")
        return None

    for banco in bancos:
        if banco.get("id") == id_banco:
            for conta in banco.get("contas", []):
                if conta.get("numero") == id_conta:
                    return conta
            print(f"Conta {id_conta} não encontrada no banco {id_banco}.")
            return None

    print(f"Banco com ID {id_banco} não encontrado.")
    return None
def depositar_em_conta(banco, numero_conta, valor, nome_arquivo="db_banco.json"):
    if valor <= 0:
        print("O valor do depósito deve ser positivo.")
        return

    if not os.path.exists(nome_arquivo):
        print(f"Arquivo {nome_arquivo} não encontrado.")
        return

    with open(nome_arquivo, "r", encoding="utf-8") as f:
        dados = json.load(f)

    banco_encontrado = False
    conta_encontrada = False

    for i, banco_dict in enumerate(dados):
        if banco_dict.get("id") == banco.id:
            banco_encontrado = True
            for j, conta_dict in enumerate(banco_dict.get("contas", [])):
                if conta_dict.get("numero") == numero_conta:
                    conta_encontrada = True
                    saldo_atual = conta_dict.get("saldo", 0)
                    novo_saldo = saldo_atual + valor
                    dados[i]["contas"][j]["saldo"] = novo_saldo
                    print(f"Depósito de R${valor:.2f} realizado na conta {numero_conta}. Saldo atualizado: R${novo_saldo:.2f}")

                    # Atualiza saldo no objeto banco, independente de dict ou objeto Conta
                    for k, c in enumerate(banco.contas):
                        numero = c.numero if hasattr(c, 'numero') else c.get('numero')
                        if numero == numero_conta:
                            if hasattr(c, 'saldo'):
                                c.saldo = novo_saldo
                            else:
                                c['saldo'] = novo_saldo
                            break
                    break
            break

    if not banco_encontrado:
        print(f"Banco com ID {banco.id} não encontrado no arquivo.")
        return

    if not conta_encontrada:
        print(f"Conta número {numero_conta} não encontrada no banco {banco.id}.")
        return

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)