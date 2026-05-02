# > LISTAS

# Antes

nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com lista

notas = [7.9, 9.7, 8.2]

# Criando listas

lista = []
lista = list()
lista = [39, 'Luciana', 9.9, True]
lista_de_listas = [10, [1, 2 ,3]]


# Indexação e Slices (fatiamento)

lista = [39, 'Luciana', 9.9, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1]) # -1 é o ultimo elemento da lista

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3]) # pega itens 0, 1 e 2 (menor que 3)
print(lista[3:6])
print(lista[3:]) # vai até o final
print(lista[2:7:2]) # o ultimo 2 é pular de 2 em 2



# > Iteração com FOR

# 1. Utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)
# para cada elemento dentro da lista ele vai imprimir o elemento
            

# 2. Utilizando os índices

#para saber quantos elementos a lista em usa a função LEN
print('Comprimento da lista:', len(lista))

# para dizer quantos elementos tem na lista 1 a 1
for i in range(len(lista)):
    print(i)

# para dizer cada elemento específico da lista

for i in range(len(lista)):
    print(lista[i]) 

# > MÉTODO DE LISTAS

lista = [1, 3, 12, 8, 2]

# append (adiciona um elemento ao final da lista)

print('Antes do append:', lista)

lista.append(3)

print('Depois do append:', lista)

# insert (vc escolhe qual elemento e a posição quer adicionar) 
# primeiro a posição e depois qual elemento

lista.insert(2, 10)

print('Depois do insert:', lista)

# extend (juntar duas listas)

lista2 = [1, 2, 3]

lista.extend(lista2)

print('Depois do extend:', lista)

# pop (remove a posicao/indice q vc escolher, se n escolher, remove o ultimo)

lista.pop()

print("Lista após o pop:", lista)

lista.pop(0)

print('Lista após o pop:', lista)

# remove (vc diz qual elemento e nao o indice/posição q quer remover)

lista.remove(3)

print('Lista após remove:', lista)

# count (conta a quantidade de elementos especificado)

print('Quantidade de 2 na lista:', lista.count(2))


# Index (diz o indice de um elemento dentro da lista)

print('Índice do elemento 12:', lista.index(12))

# Sort (para ordenar a lista na forma crescente)

lista.sort()

print(lista)

lista.sort(reverse=True) # (para ordenar a lista na forma decrescente)

print(lista)


# FUNÇÕES PARA LISTAS

# len ( quantos elementos tem na lista)

print(len(lista))

# sum (soma dos elementos da lista)

print(sum(lista))

# max ( mostra o maior valor)

print('Maior elemento da lista:', max(lista))

# min ( mostra o menor valor)

print('Menor elemento da lista:', min(lista))