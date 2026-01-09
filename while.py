inteiro = int(input("Digite um número inteiro: "))
soma = 0
while inteiro > 0:
    if inteiro % 5 != 0:
        soma += inteiro
    inteiro = int(input("Digite um número inteiro: "))
print(f"A soma dos números positivos é: {soma}")
