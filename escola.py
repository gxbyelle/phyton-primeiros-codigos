n1 = float(input("Digite sua nota do 1º período: "))
while n1 > 10 or n1 < 0:
    print("Nota inválida.")
    n1 = float(input("Digite sua nota do 1º período novamente: "))

n2 = float(input("Digite sua nota do 2º período: "))
while n2 > 10 or n2 < 0:
    print("Nota inválida.")
    n2 = float(input("Digite sua nota do 2º período novamente: "))

n3 = float(input("Digite sua nota do 3º período: "))
while n3 > 10 or n3 < 0:
    print("Nota inválida.")
    n3 = float(input("Digite sua nota do 3º período novamente: "))

n4 = float(input("Digite sua nota do 4º período: "))
while n4 > 10 or n4 < 0:
    print("Nota inválida.")
    n4 = float(input("Digite sua nota do 4º período novamente: "))

media = (n1 + n2 + n3 + n4)/4
print(f"\nSua nota final é {media:.1f}")

if media >= 7.0:
    print("Você está aprovado(a)")
elif media < 7.0 and media >= 4.0:
    print("Você tem direito a recuperação")
else:
    print("Você está reprovado(a)")
