#1.Faça um programa que mostre na tela os números de 0 até 10 usando while.

contador = 0
while contador <= 10:
    print(contador)
    contador += 1

# 2.Faça um programa que mostre na tela apenas os números pares de 2 até 20 usando while.

contador = 2
while contador <= 20:
    print(contador)
    contador += 2

#3.Faça um programa que peça ao usuário um número e depois mostre a tabuada desse número de 1 até 10 usando while.
numero = int(input("Digite um número: "))
contador = 1
while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1

#4.Faça um programa que peça ao usuário para digitar uma senha. O programa só deve parar quando ele digitar a senha correta: 1234.
senha_correta = "1234"
senha = input("Digite a senha: ")
while senha != senha_correta:
    print("Senha incorreta. Tente novamente.")
    senha = input("Digite a senha: ")
print("Senha correta. Acesso permitido.")

#5.Faça um programa que peça ao usuário um número maior que zero. Caso ele digite um valor inválido, o programa deve continuar pedindo até que ele digite um número válido.
numero = float(input("Digite um número maior que zero: "))
while numero <= 0:
    print("Número inválido. Tente novamente.")
    numero = float(input("Digite um número maior que zero: "))
print(f"Número válido: {numero}")

#6.Faça um programa que peça 5 números ao usuário e no final mostre a soma de todos eles.
soma = 0
contador = 1
while contador <= 5:
    numero = int(input("Digite um número: "))
    soma += numero
    contador += 1
print(f"Soma dos números: {soma}")

#7.Faça um programa que peça 5 números ao usuário e no final mostre a média deles.

soma = 0
contador = 1
while contador <= 5:
    numero = int(input("Digite um número: "))
    soma += numero
    contador += 1
print(f"Média dos números: {soma / 5}")

#8.Faça um programa que peça números ao usuário e continue repetindo até que ele digite 0. No final, mostre a soma de todos os números digitados.
soma = 0
numero = int(input("Digite um número (0 para parar): "))
while numero != 0:
    soma += numero
    numero = int(input("Digite um número (0 para parar): "))
print(f"Soma dos números: {soma}")