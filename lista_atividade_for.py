# 1. Faça um programa que leia um número inteiro e mostre todos os divisores desse número
num = int(input("Digite um número inteiro para mostrar seus divisores: "))
print(f"Os divisores de {num} são:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)

# 2.Faça um programa que leia um número inteiro e informe quantos divisores ele possui.
contador = 0
num = int(input("Digite um número inteiro: "))
for i in range (1, num+1) :
    if num % i == 0:
        contador += 1
print(f"O número {num} possui {contador} divisores.")

# 3 Faça um programa que leia um número inteiro e informe se ele é primo ou não.
num = int(input("Digite um número inteiro para saber se é primo ou não: "))

contador = 0

for i in range(1, num + 1):
    if num % i == 0:
        contador += 1

if contador == 2:
    print("O número é primo")
else:
    print("O número não é primo")

# 4. Faça um programa que leia 10 números inteiros e mostre a soma apenas dos números positivos
soma_positivos = 0
for i in range(10):
    num = int(input("Digite um número inteiro: "))
    if num > 0:
        soma_positivos += num
print(f"A soma dos números positivos é: {soma_positivos}")

# 5. Faça um programa que leia 10 números inteiros e mostre quantos são pares e quantos são ímpares
pares = 0
ímpares = 0
for i in range(10):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        pares += 1
    else:
        ímpares += 1
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {ímpares}")

# 6 Faça um programa que leia 8 números inteiros e informe qual foi o maior número digitado.

maior = int(input("Digite um número inteiro: "))

for i in range(7):
    num = int(input("Digite um número inteiro: "))
    if num > maior:
        maior = num

print("O maior número digitado foi:", maior)

# 7. Faça um programa que leia 8 números inteiros e informe qual foi o menor número digitado.
menor = int(input("Digite um número inteiro: "))

for i in range(7):
    num = int(input("Digite um número inteiro: "))
    if num < menor:
        menor = num

print("O menor número digitado foi:", menor)

# 8. Faça um programa que leia um número inteiro e calcule o seu fatorial.

num = int(input("Digite um número inteiro para calcular seu fatorial: "))
fatorial = 1
for i in range(1, num + 1):
    fatorial *= i
print(f"O fatorial de {num} é: {fatorial}")

# 9. Faça um programa que leia um número inteiro e mostre a tabuada dele de 1 até 20, exibindo apenas os resultados pares.
num = int(input("Digite um número inteiro para mostrar a tabuada de 1 a 20 (apenas resultados pares): "))
for i in range(1, 21):
    resultado = num * i
    if resultado % 2 == 0:
        print(f"{num} x {i} = {resultado}")

# 10. Faça um programa que leia 10 números inteiros e calcule a média apenas dos números maiores que zero. Caso nenhum número positivo seja digitado, mostre uma mensagem informando que não foi possível calcular a média.
soma = 0
contador = 0
for i in range(10):
    num = int(input("Digite um número inteiro: "))
    if num > 0:
        soma += num
        contador += 1
if contador > 0:
    media = soma / contador
    print(f"A média dos números positivos é: {media}")
else:
    print("Não foi possível calcular a média, pois nenhum número positivo foi digitado.")