import math
import os 

x = 4
angulo = 30
pasta = os.getcwd()
lista1 = [1, 2, 3, 4, 7, 0]
raiz = math.sqrt(x)
seno = math.sin(angulo)
lista3 = len(lista1)
soma = sum(lista1)

print(f"\nA raiz quadrada de {x} é igual a {raiz}")   
print(f"O seno de {angulo} é igual a {seno}")
print(f"Os códigos estão no seguinte diretório: {pasta}")
print(f"A lista {lista1} tem {lista3} elementos")
print(f"A lista {lista1} tem {soma} de soma total\n")

# os.system("cls")
