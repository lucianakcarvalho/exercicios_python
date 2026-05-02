nota = float(input("Digite sua nota: "))

if nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")



idade = int(input("Digite sua idade"))


if idade >= 18:
    print("Você é maior de idade")
elif idade > 14 and idade < 17:
    print("Adolescente")
elif idade > 0 and idade <= 13:
    print("Criança")
else:
    print("Valor invalido")


nota = float(input("Digite sua nota"))

if nota >= 7 :
    print("Aprovado")
elif nota > 0 and nota < 7:
    print("Reprovado")
else:
    print("Nota inválida")



numero = float(input("Digite seu número: "))

if numero > 0:
    print("positivo")
elif numero == 0:
    print("neutro")
else:
    print("negativo")



senhaCerta = 1234

senha = int(print("Digite sua senha: "))

if senha == senhaCerta:
    print("Acesso permitido")
else:
    print("Acesso negado")



valorCompra = float(input("Digite o valor da compra: "))

if valorCompra >= 100:
    print("Valor maior que 100")
else:
    print("Menor que 100")



num1 = int(input("Digite o primeiro numero "))
num2 = int(input("Digite o segundo numero: "))

if num1 > num2:
    print("ele é maior")
elif num1 == num2:
    print("São iguais")
else:
    print("ele é menor")
