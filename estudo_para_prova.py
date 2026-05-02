numero = int(input("Digite um numero: "))
  
if numero % 2 == 0:
  print("O numero é par ")
else:
  print("O numero é impar")

#Faça um programa que:

#Leia 3 números
#Mostre qual é o maior e qual é o menor

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))


maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

print("Maior:", maior)
print("Menor:", menor)

#tabuada
num = int(input("Digite um número: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


idade = int(input("digite sua idade: "))

if idade >= 18:
  print("Voce eh maior de idade")
else:
  print("Voce eh menor de idade")

'''Leia um número e informe:

Positivo
Negativo
Zero'''

numero = int(input("digite um numero: "))
if numero > 0:
   print("numero eh positivo")
elif numero < 0:
   print("numero negativo")
else:
   print("o numero eh 0")

#Leia dois números e informe qual é o maior.
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("digite o segundo numero: "))

maior = max(num1, num2)
menor = min(num1, num2)

print("o maior é: ", maior)
print("o menor é: ", menor)

#Leia a nota de um aluno e informe:

nota = float(input("Digite sua nota: "))

if nota >= 7:
  print("aprovado")
elif nota >= 5:
  print("recuperação")
else:
  print("reprovado")

'''Crie um sistema que:

Usuário correto: "admin"
Senha correta: "1234"
Informe se o acesso foi permitido ou negado'''

login_certo = "admin"
senha_certa = 1234
login = input("Digite seu login: ")
senha = int(input("Digite sua senha: "))

if login == login_certo and senha == senha_certa:
  print("acesso permitido")
else:
  print("Acesso negado")