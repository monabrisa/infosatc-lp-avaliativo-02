num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))
num4 = int(input("Digite o quarto e último número inteiro: "))

lista = [num1, num2, num3, num4]

soma = sum(lista)

print ("A soma dos números listados é: {}".format(soma))