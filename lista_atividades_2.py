#1. Faça um programa que leia a idade de uma pessoa e informe se ela pode votar, considerando idade mínima de 16 anos.

idadeMinima = int(input("Digite sua idade: "))


if idadeMinima >= 16:
    print("Você já pode votar")
else:
    print("Você ainda não pode votar")


#2. Faça um programa que leia a temperatura e informe se está quente ou frio, considerando quente quando for maior que 30 graus.

temperatura = float(input("Digite a temperatura: "))


if temperatura > 30:
    print("Está quente")
else:
    print("Está frio")


#3. Faça um programa que leia o salário de uma pessoa e informe se ela recebe acima de 2000 reais ou 2000 reais ou menos.

salario = float(input("Digite seu salario: "))


if salario > 2000:
    print("Você recebe mais de R$ 2000")
elif salario == 2000:
    print("Você recebe R$ 2000")
else:
    print("Você recebe menos de R$ 2000")


#4. Faça um programa que leia um número e informe se ele é par ou ímpar.

numero = int(input("Digite um numero: "))


if numero % 2 == 0:
    print("O numero é par")
else:
    print("O numero é impar")


#5. Faça um programa que leia o nome de um aluno e sua nota, informando se ele foi aprovado ou reprovado.

nome = input("Digite seu nome: ")
nota = float(input("Digite sua nota: "))

if nota >= 7:
    print(nome + ", você foi aprovado!")
else:
    print(nome + ", você foi reprovado")


#6. Faça um programa que leia a idade de uma pessoa e informe se ela pode entrar no evento, considerando entrada permitida apenas para maiores de 18 anos.

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você pode entrar no evento!")
else:
    print("Você não pode entrar no evento!")

#7. Faça um programa que leia um número e informe se ele é maior que 10 ou menor ou igual a 10.

numero = int(input("Digite um numero: "))

if numero > 10:
    print("O numero é maior que 10")
elif numero == 10:
    print("O numero é igual a 10")
else:
    print("O numero é menor que 10")

#8. Faça um programa que leia a quantidade de faltas de um aluno e informe se ele está dentro do limite ou acima do limite, considerando limite de 10 faltas.

faltas = int(input("Digite o numero de faltas: "))

if faltas > 10:
    print("Você está acima do limite de faltas")
else:
    print("Você está dentro do limite de faltas")


#9. Faça um programa que leia uma senha e informe se ela está correta ou incorreta, considerando a senha python123.

senhaCerta = "python123"

senha = input("Digite sua senha: ")

if senha == senhaCerta:
    print("Senha correta, acesso permitido")
else:
    print("Senha errada, acesso negado")

#10. Faça um programa que leia dois números e informe qual deles é o maior, ou se eles são iguais.

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 > numero2:
    print("O numero", numero1, "é maior que", numero2)
elif numero2 > numero1:
    print("O numero", numero2, "é maior que", numero1)
else:
    print("Os numeros são iguais")