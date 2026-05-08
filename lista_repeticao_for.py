#1 Faça um programa que mostre na tela os números de 1 até 20 usando for.

for i in range(1, 21):
    print(i)




#2 Faça um programa que mostre os números de 30 até 1 usando for.

for i in range(30, 0, -1):
    print(i)


#3 Faça um programa que mostre todos os números pares de 1 até 50 usando for.

for i in range(1, 51):
    if i % 2 == 0:
        print(i)


#4 Faça um programa que mostre todos os números ímpares de 1 até 50 usando for.

for i in range(1, 51):
    if i % 2 != 0:
        print(i)


#5 Faça um programa que leia um número inteiro e mostre a tabuada desse número de 1 até 10 usando for.


num = int(input("Digite um número para mostrar a tabuada: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


#6 Faça um programa que calcule e mostre a soma dos números de 1 até 100 usando for.

for i in range(1, 101):
    soma = 0
    soma += i
    print(f"A soma dos números de 1 a 100 é: {soma}")



#7 Faça um programa que calcule e mostre a soma de todos os números pares de 1 até 100 usando for e if.

soma_pares = 0
for i in range(1, 101):
    if i % 2 == 0:
        soma_pares += i
    print(f"A soma dos números pares de 1 a 100 é: {soma_pares}")

#8 Faça um programa que conte quantos números entre 1 e 100 são múltiplos de 3. No final, mostre a quantidade encontrada.

contador_multiplos_3 = 0
for i in range(1, 101):
    if i % 3 == 0:
        contador_multiplos_3 += 1
        print(f"A quantidade de números entre 1 e 100 que são múltiplos de 3 é: {contador_multiplos_3}")


#9 Faça um programa que mostre todos os números de 1 até 200 que são divisíveis por 5. Use for e if.

for i in range(1, 201):
    if i % 5 == 0:
        print(i)

#10 Faça um programa que leia 10 números inteiros e conte quantos deles são positivos, negativos e iguais a zero. No final, mostre a quantidade de positivos, negativos e zeros.'''

contador_negativos = 0
contador_positivos = 0
contador_zeros = 0
for i in range(10):
    num = int(input("Digite um número inteiro: "))
    if num > 0:
        contador_positivos += 1
    elif num < 0:
        contador_negativos += 1
    else:
        contador_zeros += 1
print(f"Quantidade de números positivos: {contador_positivos}")
print(f"Quantidade de números negativos: {contador_negativos}")
print(f"Quantidade de números iguais a zero: {contador_zeros}")
    