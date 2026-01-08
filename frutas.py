numero = int(input("Quantas frutas você comprou? "))

if numero != 0:
      maior = numero
      menor = numero
else:
    maior = 0
    menor = 0

frutas = 0
clientes = 0

while numero != 0:
    frutas += numero
    clientes += 1

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

    numero = int(input("Quantas frutas você comprou? "))

print(f"Foram compradas {frutas} frutas por {clientes} clientes.\nO maior comprador comprou {maior} frutas e o menor comprou {menor} frutas.")
