# > DICIONÁRIOS

# 1. Criando dicionários

dicionario = {}
dicionario = dict()

dicionario = { 'nome': 'Luciana', 'idade': 39, 'altura': 1.58} 

print(dicionario)
print(dicionario['idade'])
print(dicionario['nome'])
print(dicionario['altura'])


# Adicionando elementos em um dicionário

dicionario['programador'] = True

print(dicionario)

dicionario['altura'] = 2

print(dicionario)


# Iterando sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave])


# Testando a existência de uma chave

print('peso' in dicionario)
print('altura' in dicionario)