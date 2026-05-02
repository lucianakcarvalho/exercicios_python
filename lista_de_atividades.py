#1.Crie um programa que peça o nome de uma pessoa, o curso em que ela estuda e o período atual, 
# e depois mostre todas essas informações em uma frase organizada.

nome = input("Digite seu nome: ")
curso = input("Digite o curso que você estuda: ")
periodo = int(input("Digite seu período atual: "))
print("Olá,", nome, ", seu curso é:", curso, ", você está no", periodo,"º período.")

#2. Faça um programa que solicite três números inteiros e mostre a soma total entre eles.

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))
soma = num1 + num2 +num3
print("A soma dos três numeros é: ", soma)

#3. Elabore um programa que peça um número decimal e mostre a terça parte desse valor

num = float(input("Digite um numero decimal: "))
result = num / 3
print(result)

#4. Crie um programa que peça ao usuário a quantidade de quilômetros percorridos e a quantidade
# de litros de combustível gastos, e depois mostre o consumo médio do veículo.

km = float(input("Digite a quantidade de quilometros percorridos: "))
litros = float(input("Digite a quantidade de litros de combustível gastos: "))
consumo_medio = (km + litros) / 2
print("O consumo médio do seu veiculo foi de: ", consumo_medio)

#5.Faça um programa que peça o salário de um funcionário e mostre quanto ele receberá 
# caso tenha um aumento de 15%

salario = float(input("Digite seu salário: " ))
aumento = salario * 0.15
novo_salario = salario + aumento
print("Seu novo salário com aumento de 15% é de: R$", novo_salario)


#6.Desenvolva um programa que peça a idade de uma pessoa e mostre quantos meses de vida
# ela possui aproximadamente.

idade = int(input("Digite sua idade: "))
meses = idade * 12
print("Você já viveu aproximadamente", meses, "meses")

#7.Crie um programa que peça a base e a altura de um triângulo, calcule sua área e mostre
# o resultado na tela.

base = float(input("Digite a base do triangulo: "))
altura = float(input("Digite a altura do triangulo: "))
area = (base * altura) / 2
print("A area do triangulo é: ", area)


#8.Faça um programa que peça o valor de um produto e o percentual de desconto, calculando
# quanto o produto passará a custar após o desconto.

valor = float(input("Digite o valor do produto:  "))
percentual = float(input("Digite o percentual de desconto: "))

desconto = valor * (percentual / 100)
valor_final = valor - desconto
print("O produto passará a custar R$", valor_final, "após o desconto")


#9.Elabore um programa que peça ao usuário uma temperatura em graus Celsius e mostre o
# valor correspondente em Fahrenheit.

celsius = float(input("Digite a temperatura em graus Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("A temperatura em Fahrenheit é: ",fahrenheit,"°F")

#10. Crie um programa que peça o nome do aluno e três notas, calcule a média final e mostre
# uma mensagem com o nome do aluno e sua média.

nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print("O aluno" ,nome, "tem média final de: ",media)

