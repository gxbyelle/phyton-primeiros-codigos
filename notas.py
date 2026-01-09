print("\nBem vindo ao PORTAL DE NOTAS do COLÉGIO ARBOS")
nome = input("Nome completo: ")
turma = input("Turma: ")

n1 = float(input("\nDigite sua nota do 1º período: "))

while n1 < 0 or n1 > 10:
    n1 = float(input("\nNota inválida. Digite sua nota do 1º período: "))

n2 = float(input("Ótimo, agora digite sua nota do 2º período: "))

while n2 < 0 or n2 > 10:
    n2 = float(input("\nNota inválida. Digite sua nota do 2º período: "))

n3 = float(input("Certinho. Digite sua nota do 3º período: "))

while n3 < 0 or n3 > 10:
    n3 = float(input("\nNota inválida. Digite sua nota do 3º período: "))

n4 = float(input("Para finalizar, digite sua nota do 4º período: "))

while n4 < 0 or n4 > 10:
    n4 = float(input("\nNota inválida. Digite sua nota do 4º período: "))

media = (n1 + n2 + n3 + n4) / 4

print("\nAluno(a):", nome)
print("Turma:", turma)
print("\nNotas:")
print(f"1º período: {n1:.1f}")
print(f"2º período: {n2:.1f}")
print(f"3º período: {n3:.1f}")
print(f"4º período: {n4:.1f}")
print(f"\nMédia final: {media:.1f}")

if media >= 7:
    print("Situação: Aprovado(a)\n")

elif media >= 4:
    print("Situação: Recuperação\n")

else:
    print("Situação: Reprovado(a)\n")

