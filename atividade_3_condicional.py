'''1 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
Três números em ordem decrescente.'''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 > num2 and num1 > num3:
  print(num1)
  if num2 > num3:
    print(num2)
    print(num3)
  else:
    print(num3)
    print(num2)
    
elif num2 > num1 and num2 > num3:
  print(num2)
  if num3 > num1:
    print(num3)
    print(num1)
  else:
    print(num1)
    print(num3)
else:
  print(num3)
  if num1 > num2:
    print(num1)
    print(num2)
  else:
    print(num2)
    print(num1)


''' 2- Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

turno = input("Qual turno você estuda? Digite (M) para matutino, (V) para vespertino ou (N) para noturno ")

if turno == "M" or turno == "m":
  print("Bom Dia!")
elif turno == "V" or turno == "v":
  print("Boa Tarde!")
elif turno == "N" or turno == "n":
  print("Boa Noite!")
else:
  print("Valor inválido")

'''3 - Faça um programa que recebe o salário de um colaborador e o reajuste     segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.'''

salario = float(input("Digite o seu salário "))

if salario <= 280:
  percentual = 0.2
  valorAumento = salario * percentual
  novoSalario = salario + valorAumento

elif salario > 280 and salario <= 700:
  percentual = 0.15
  valorAumento = salario * percentual
  novoSalario = salario + valorAumento

elif salario > 700 and salario <= 1500:
  percentual = 0.1
  valorAumento = salario * percentual
  novoSalario = salario + valorAumento

else:
  percentual = 0.05
  valorAumento = salario * percentual
  novoSalario = salario + valorAumento

print("Seu salário atual é: ", salario)
print("O percentual de aumento aplicado foi de ", percentual * 100, "%")
print("O valor do aumento foi de: ", valorAumento)
print("Seu novo salário após aumento é de: ", novoSalario)

'''4 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%


Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

    Salário Bruto: (5 * 220)        : R$ 1100,00
    (-) IR (5%)                                : R$   55,00 
    (-) INSS ( 10%)                       : R$  110,00
    FGTS (11%)                            : R$  121,00
    Total de descontos                : R$  165,00
    Salário Líquido                       : R$  935,00'''
valorHora = float(input("Digite o valor da sua hora: "))
horaTrabalhada = float(input("Digite a quantidade de horas trabalhadas no mês:"))

salario = valorHora * horaTrabalhada

if salario <= 900:
  sindicato = salario * 0.03
  fgts = salario * 0.11
  ir = "Isento"
  percentual = 0
  

elif salario > 900 and salario <= 1500:
  sindicato = salario * 0.03
  fgts = salario * 0.11
  percentual = 0.05
  ir = salario * percentual


elif salario > 1500 and salario <= 2500:
  sindicato = salario * 0.03
  fgts = salario * 0.11
  percentual = 0.1
  ir = salario * percentual

else:
  sindicato = salario * 0.03
  fgts = salario * 0.11
  percentual = 0.2
  ir = salario * percentual

print("Salário Bruto: (", horaTrabalhada, "*", valorHora, ")" , salario)
print("(-) IR (", percentual * 100, "%)", ir)
print("FGTS (11%)", fgts)
print("Total de descontos", sindicato + ir)
print("Salário Líquido", salario - sindicato - ir)

'''5 - Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

dia = int(input("Digite o dia um numero de 1 a 7: "))

if dia == 1:
  print("Domingo")
elif dia == 2:
  print("Segunda")
elif dia == 3:
  print("Terça")
elif dia == 4:
  print("Quarta")
elif dia == 5:
  print("Quinta")
elif dia == 6:
  print("Sexta")
elif dia == 7:
  print("Sábado")
else:
  print("Valor inválido")

'''6 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0                      A
      Entre 7.5 e 9.0                        B
      Entre 6.0 e 7.5                        C
      Entre 4.0 e 6.0                        D
      Entre 4.0 e zero                      E
    O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''



nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9.0 and media <= 10.0:
  conceito = "A"
  mensagem = "Aprovado"

elif media >= 7.5 and media < 9.0:
  conceito = "B"
  mensagem = "Aprovado"

elif media >= 6.0 and media < 7.5:
  conceito = "C"
  mensagem = "Aprovado"

elif media >= 4.0 and media < 6.0:
  conceito = "D"
  mensagem = "Reprovado"
  
elif media >= 0.0 and media < 4.0:
  conceito = "E"
  mensagem = "Reprovado"

print("Nota 1: ", nota1)
print("Nota 2: ", nota2)
print("Média: ", media)
print("Conceito: ", conceito)
print(mensagem)

'''7 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
    Código comentado: Triângulos em Python'''

lado1 = float(input("Digite o lado 1 do triangulo: "))
lado2 = float(input("Digite o lado 2 do triangulo: "))
lado3 = float(input("Digite o lado 3 do triangulo: "))

ehTriangulo = False
ehIsosceles = False
ehEquilatero = False
ehEscaleno = False



if (lado1 + lado2) > lado3:
  ehTriangulo = True
elif (lado2 + lado3) > lado1:
  ehTriangulo = True
elif (lado1 + lado3) > lado2:
  ehTriangulo = True

if lado1 == lado2 and lado2 == lado3 and lado3 == lado1:
  ehEquilatero = True
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
  ehIsosceles = True
elif lado1 != lado2 and lado2 != lado3 and lado3 != lado1:
  ehEscaleno = True

if ehTriangulo:
  if ehEquilatero:
    print("É triângulo equilátero")
  elif ehIsosceles:
    print("É triângulo isosceles")
  elif ehEscaleno:
    print("É triângulo escaleno")
else:
  print("Não é um triangulo")

'''8 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.'''

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Ano bissexto")
else:
    print("Não é ano bissexto")