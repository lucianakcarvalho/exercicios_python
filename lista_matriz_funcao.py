# MATRIZ

#1. Crie uma matriz 3x3 com valores digitados pelo usuário. Depois, mostre a matriz na tela em formato de tabela.

matriz = []

for i in range(3):
  linha = []
  for j in range(3):
    valor = int(input('Digite um valor: '))
    linha.append(valor)
  matriz.append(linha)

print('\nMatriz:')

for linha in matriz:
    for valor in linha:
        print(valor, end='\t')
    print()

# 2. Crie uma matriz 2x3 com números inteiros digitados pelo usuário. Depois, mostre a soma de todos os valores da matriz.

matriz = []
soma = 0

for i in range(2):
  linha = []
  for j in range(3):
    valor = int(input('Digite um valor: '))
    linha.append(valor)
    soma += valor
  matriz.append(linha)

print('Soma de todos os valores:', soma)


# 3. Crie uma matriz 3x3 com números inteiros. Depois, mostre o maior valor da matriz.

matriz = []

for i in range(3):
  linha = []
  for j in range(3):
    valor = int(input('Digite um valor: '))
    linha.append(valor)
  matriz.append(linha)

maior = matriz[0][0]

for linha in matriz:
    for valor in linha:
        if valor > maior:
            maior = valor

print('O maior valor da matriz é:', maior)


#4. Crie uma matriz 3x3 com números inteiros. Depois, mostre o menor valor da matriz

matriz = []

for i in range(3):
  linha = []
  for j in range(3):
    valor = int(input('Digite um valor: '))
    linha.append(valor)
  matriz.append(linha)

menor = matriz[0][0]

for linha in matriz:
    for valor in linha:
        if valor < menor:
            menor = valor

print('O menor valor da matriz é:', menor)


#5. Crie uma matriz 3x3 e mostre apenas os valores da diagonal principal.

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input('Digite um valor: '))
        linha.append(valor)
    matriz.append(linha)

print('Diagonal principal:')

for i in range(3):
    print(matriz[i][i])

#6. Crie uma matriz 3x3 e calcule a soma dos valores da diagonal principal.

matriz = []
soma = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input('Digite um valor: '))
        linha.append(valor)
    matriz.append(linha)

for i in range(3):
    soma += matriz[i][i]

print('Soma da diagonal principal:', soma)

#7. Crie uma matriz 3x3 e conte quantos números pares existem dentro dela.

matriz = []
pares = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input('Digite um valor: '))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    for valor in linha:
      pares += 1

print('Quantidade de números pares:', pares)

# 8. Crie uma matriz 3x3 e conte quantos números são maiores que 10.

matriz = []
contador = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input('Digite um valor: '))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    for valor in linha:
        if valor > 10:
            contador += 1

print('Quantidade de números maiores que 10:', contador)

#9. Crie uma matriz para armazenar 3 notas de 4 alunos. Depois, calcule e mostre a média de cada aluno.

matriz = []

for i in range(4):
    linha = []
    print(f'Aluno {i+1}')
    
    for j in range(3):
        nota = float(input(f'Digite a nota {j+1}: '))
        linha.append(nota)
    
    matriz.append(linha)

print('\nMédias dos alunos:')

for i in range(4):
    media = sum(matriz[i]) / 3
    print(f'Aluno {i+1}: {media}')

#10. Crie uma matriz 3x3. Depois, mostre a soma de cada linha separadamente.

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input('Digite um valor: '))
        linha.append(valor)
    matriz.append(linha)

print('\nSoma de cada linha:')

for i in range(3):
    soma = sum(matriz[i])
    print(f'Linha {i+1}: {soma}')


# FUNÇÃO

# 11. Crie uma função chamada mensagem que mostre na tela a frase “Olá, mundo!”. Depois, chame essa função no programa principal.

def mensagem():
    print('Olá, mundo!')

mensagem()

# 12. Crie uma função chamada boas_vindas que mostre a frase “Bem-vindo à aula de Python!”. Depois, chame essa função duas vezes.

def boas_vindas():
    print('Bem-vindo à aula de Python!')

boas_vindas()
boas_vindas()

# 13. Crie uma função chamada mostrar_nome que receba um nome como parâmetro e mostre o nome informado pelo usuário.

def mostrar_nome(nome):
    print("Nome informado:", nome)

usuario = input("Digite seu nome: ")

mostrar_nome(usuario)

#14.Crie uma função chamada somar que receba dois números como parâmetro e mostre a soma entre eles.

def somar(a, b):
    return a + b

resultado = somar(5, 7)

print('O resultado da soma é: ', resultado)

#15. Crie uma função chamada subtrair que receba dois números como parâmetro e mostre a subtração entre eles.

def subtrair(a, b):
    return a + b

resultado = subtrair(5, 7)

print('O resultado da subtração é: ', resultado)

#16. Crie uma função chamada mostrar_dobro que receba um número como parâmetro e mostre o dobro desse número

def mostrar_dobro(a):
    return a * 2

num = int(input('Digite um número: '))

print('O dobro de', num, 'é: ', mostrar_dobro(num))

#17. Crie uma função chamada verificar_idade que receba uma idade como parâmetro e informe se a pessoa é maior ou menor de idade.

def verificar_idade(a):
    if a >= 18:
        print('Você é maior de idade')
    else:
        print('Você é menor de idade')

idade = int(input('Digite sua idade: '))

verificar_idade(idade)

#18. Crie uma função chamada verificar_positivo que receba um número como parâmetro e informe se ele é positivo, negativo ou zero.

def verificar_positivo(a):
    if a > 0:
        return 'positivo'
    elif a < 0:
        return 'negativo'
    else:
        return 'zero'

num = int(input('Digite um número: '))

print('O numero', num, 'é', verificar_positivo(num))

#19. Crie uma função chamada calcular_media que receba duas notas como parâmetro e mostre a média entre elas.

def calcular_media(a, b):
    media = (a + b) / 2
    return media

nota1 = float(input('Digite sua 1ª nota: '))
nota2 = float(input('Digite sua 2ª nota: '))

print('A média das notas é: ', calcular_media(nota1, nota2))

#20. Crie uma função chamada verificar_situacao que receba uma média como parâmetro e informe se o aluno está aprovado ou reprovado, considerando aprovado quem tiver média maior ou igual a 7.

def verificar_situacao(media):
    if media >= 7:
        return 'aprovado'
    else:
        return 'reprovado'
    
media = float(input('Digite sua média: '))

print('Você está', verificar_situacao(media))
