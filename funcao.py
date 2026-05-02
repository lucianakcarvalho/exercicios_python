# . FUNÇÕES

# 1. O que são funções e por que utilizá-las?

# Funções que já utilizamos anteriormente...


"""print() # imprime uma mensagem (int, floar, str) no console (terminal)
input() # retorna um dado informado pelo usuário (entrada padrão) e pode receber uma string
len() # recebe uma lista e retorna o tamanho dessa lista
max() # retorna o maior valor de uma lista"""

# 2. Criação de funções

# Função inicial

def saudacao():
    print('Seja bem vindo(a)!')
    print('Olá, é um prazer ter você fazendo parte desse curso!')

saudacao()

# Função com parâmentros

def saudacao(nome, curso):
    print(f'Seja bem vindo(a), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao('Luciana', 'Python')

# Função com parâmetros default

def saudacao(nome, curso='Python'):
    print(f'Seja bem vindo(a), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao('Luciana', 'C++')


# Funções com retorno

def soma(num1, num2):
    print('Soma =', num1 + num2)

soma(5, 7)

def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)

print('O resultado da soma é: ', resultado)


def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1-num2
    elif operacao == '*':
        return num1*num2
    elif operacao == '/':
        return num1/num2

print(resultado)