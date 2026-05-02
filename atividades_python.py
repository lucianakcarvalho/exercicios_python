# 1 crie um programa que peça o nome do aluno e sua idade, e depois mostre uma mensagem apresentando essas
# informações na tela, dizendo quem é ele e quantos anos possui


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print("Seu nome é", nome, "2 sua idade é", idade)


#2 faça um programa que peça ao usuario dois numeros inteiros e mostre na tela o resultado da soma 
#entre eles

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
result = num1 + num2
print(result)


#3 elabore um programa que solicite um numero ao usuario e mostre o dobro, o triplo e a metade desse numero


num1 = int(input("Digite o numero desejado: "))
dobro = num1 * 2
triplo = num1 * 3
metade = num1 / 2
print(dobro, triplo, metade)

#4 Crie um programa que peça ao aluno duas notas, calcule a media aritmetica entre elas e mostre
# o resultado final na tela

nt1 = float(input("Digite sua primeira nota: "))
nt2 = float(input("Digite sua segunda nota: "))
media = (nt1 + nt2) / 2
print(media)


#5 Faça um programa que peça o valor de um produto e mostre esse mesmo valor com um acrescimo 
# de 10%

produto = float(input("Digite o valor do produto: "))
novo_valor = produto * 1.1
print(novo_valor)

#6 desenvolva um programa que peça a largura e altura de um retangulo, calcule a area e mostre 
# o resultado ao usuario

altura = float(input("Digite sua altura: "))
largura = float(input("Digite sua largura: "))
area = altura * largura
print(area)