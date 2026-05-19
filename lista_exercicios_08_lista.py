'''1. Maior número e sua posição
Faça um programa que leia 8 números e armazene em uma lista. Depois, mostre o maior número digitado e a posição em que ele aparece na lista.'''

lista = []

for i in range(8):
    num = int(input("Digite um número: "))
    lista.append(num)

maior = lista[0]
posicao = 0

for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]
        posicao = i

print("Maior número:", maior)
print("Posição:", posicao)
    
'''2. Separar pares e ímpares
Faça um programa que leia 10 números e armazene em uma lista. Depois, crie duas novas listas: uma contendo os números pares e outra contendo os números ímpares.
No final, mostre as três listas:
Lista original: [...]
Pares: [...]
Ímpares: [...]
'''

numeros = []

for i in range(10):
    num = int(input("Digite um número: "))
    numeros.append(num)

pares = []
ímpares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        ímpares.append(num)

print("Lista original:", numeros)
print("Pares:", pares)
print("Ímpares:", ímpares)


'''3. Média e valores acima da média
Faça um programa que leia 6 notas e armazene em uma lista. Depois, calcule a média da turma e mostre quais notas ficaram acima da média.
'''
notas = []

for i in range(6):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
acima_da_media = []

for nota in notas:
    if nota > media:
        acima_da_media.append(nota)

print("Média da turma:", media)
print("Notas acima da média:", acima_da_media)

'''4. Contagem de números positivos, negativos e zeros
Faça um programa que leia 10 números e armazene em uma lista. Depois, mostre:
Quantidade de positivos
Quantidade de negativos
Quantidade de zeros
'''

numeros = []

for i in range(10):
    num = int(input("Digite um número: "))
    numeros.append(num)

positivos = 0
negativos = 0
zeros = 0

for num in numeros:
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        zeros += 1

print("Quantidade de positivos:", positivos)
print("Quantidade de negativos:", negativos)
print("Quantidade de zeros:", zeros)  

'''5. Verificar se existem números repetidos
Faça um programa que leia 8 números e armazene em uma lista. Depois, informe se existem números repetidos na lista.
Exemplo:
Existem números repetidos.
ou
Não existem números repetidos.
'''

numeros = []

for i in range(8):
    num = int(input("Digite um número: "))
    numeros.append(num)

repetido = False

for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] == numeros[j]:
            repetido = True

if repetido:
    print("Existem números repetidos.")
else:
    print("Não existem números repetidos.")

'''6. Inverter a lista sem usar reverse
Faça um programa que leia 7 números e armazene em uma lista. Depois, crie uma nova lista com os valores na ordem inversa.
Atenção: não use reverse().'''

numeros = []

for i in range(7):
    num = int(input("Digite um número: "))
    numeros.append(num)

inversa = []

for i in range(len(numeros) - 1, -1, -1):
    inversa.append(numeros[i])

print("Lista original:", numeros)
print("Lista inversa:", inversa)


'''7. Soma dos números pares e soma dos números ímpares
Faça um programa que leia 10 números e armazene em uma lista. Depois, calcule separadamente:
Soma dos pares
Soma dos ímpares
'''

numeros = []

for i in range(10):
    num = int(input("Digite um número: "))
    numeros.append(num)
soma_pares = 0
soma_impares = 0

for num in numeros:
    if num % 2 == 0:
        soma_pares += num
    else:
        soma_impares += num

print("Soma dos pares:", soma_pares)
print("Soma dos ímpares:", soma_impares)

'''8. Buscar número e mostrar quantas vezes aparece
Faça um programa que leia 10 números e armazene em uma lista. Depois, peça ao usuário um número para pesquisar.
O programa deve informar quantas vezes esse número aparece na lista.
'''
numeros = []

for i in range(10):
    num = int(input("Digite um número: "))
    numeros.append(num)

num_pesquisado = int(input("Digite o número a ser pesquisado: "))
contagem = 0

for num in numeros:
    if num == num_pesquisado:
        contagem += 1

print(f"O número {num_pesquisado} aparece {contagem} vezes na lista.")

'''9. Criar uma lista apenas com números maiores que 10
Faça um programa que leia 8 números e armazene em uma lista. Depois, crie uma nova lista contendo apenas os números maiores que 10.
No final, mostre:
Lista original: [...]
Números maiores que 10: [...]
'''
numeros = []

for i in range(8):
    num = int(input("Digite um número: "))
    numeros.append(num)

maiores_que_10 = []

for num in numeros:
    if num > 10:
        maiores_que_10.append(num)

print("Lista original:", numeros)
print("Números maiores que 10:", maiores_que_10)

'''10. Sistema simples de notas
Faça um programa que leia o nome e a nota de 5 alunos. Os nomes devem ser armazenados em uma lista e as notas em outra lista.
Depois, o programa deve mostrar:
Nome do aluno
Nota
Situação: Aprovado ou Reprovado
Considere aprovado quem tiver nota maior ou igual a 7.
'''
nomes = []
notas = []

for i in range(5):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    nomes.append(nome)
    notas.append(nota)

for i in range(5):
    print(f"Nome: {nomes[i]}, Nota: {notas[i]}")
    if notas[i] >= 7:
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")