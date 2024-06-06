pessoa = {
    'nome':'Rebeca',
    'sobrenome':'Carvalhedo'
}


print(pessoa.__len__())
print("--------")
print(pessoa.keys())
print("--------")
print(pessoa.values())
print("--------")
print(pessoa.items())
print("----Seta um item quando nao tem----")
print(pessoa.setdefault('idade',10))
print(pessoa.items())
print("----Copia objeto----")
pessoa1 = pessoa.copy()
print(pessoa1.items())
print("--------")
print(pessoa.get('nome'))
print("----Retira chave escolhida----")
print(pessoa1.pop('nome'))
print(pessoa1.items())
print("----Retira ultima chave ----")
ultima_chave = pessoa1.popitem()
print(pessoa1.items())
print("--------")
print(pessoa.update())