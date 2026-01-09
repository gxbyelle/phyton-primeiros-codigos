inteiro = int(input("Digite um número inteiro: "))

soma = 0
contador = 0
ignorados = 0
media = 0
maior = 0
menor = 0

while inteiro > 0:
    if inteiro % 5 != 0:
        soma += inteiro
        contador += 1
        media = soma / contador

        if contador == 1:
            maior = inteiro
            menor = inteiro

        else:
            if inteiro > maior:
                maior = inteiro

            if inteiro < menor: 
                menor = inteiro
    else:
        ignorados += 1
    inteiro = int(input("Digite um número inteiro: "))

print(f"\nA soma dos números positivos não multiplos de 5 é: {soma}")
print(f"Você digitou {contador} números positivos não multiplos de 5.")
print(f"{ignorados} números foram ignorados.")

if contador > 0:
    print(f"A média dos números positivos não multilplos de 5 é: {media:.2f}.")
    print(f"O maior número digitado não multiplo de 5 foi: {maior}.")
    print(f"O menor número digitado positivo não multiplo de 5 foi: {menor}.")
    
else:
    print("Você não digitou nenhum número valido")
