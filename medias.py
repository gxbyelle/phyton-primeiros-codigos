# Informações
aluno_nome = "Gabrielle Morila Mota"
aluno_senha = "041109"
aluno_turma = "1ºEMB"

# Biologia P1
nota_biologia_p1_ab = 7.8
nota_biologia_p1_aq = 2.7
nota_biologia_p1_tg = 6.8
nota_biologia_p1_ti = 6.9
nota_biologia_p1_ap1 = 4.6

media1_biologia_p1 = (nota_biologia_p1_ap1 + nota_biologia_p1_ti + nota_biologia_p1_tg) / 3
media2_biologia_p1 = (media1_biologia_p1 + nota_biologia_p1_aq + nota_biologia_p1_ab) / 2

# Biologia P2
nota_biologia_p2_ab = 5.9
nota_biologia_p2_aq = 2.0
nota_biologia_p2_sim = 4.8
nota_biologia_p2_tg = 6.5
nota_biologia_p2_ti = 7.0
nota_biologia_p2_ap1 = 4.2

media1_biologia_p2 = (nota_biologia_p2_ap1 + nota_biologia_p2_ti + nota_biologia_p2_tg) / 3
media2_biologia_p2 = (media1_biologia_p2 + nota_biologia_p2_aq + nota_biologia_p2_ab + nota_biologia_p2_sim) / 3

# Biologia P3
nota_biologia_p3_ab = 7.4
nota_biologia_p3_aq = 2.5
nota_biologia_p3_sim = 5.3
nota_biologia_p3_tg = 6.5
nota_biologia_p3_ap1 = 2.8

media1_biologia_p3 = (nota_biologia_p3_ap1 + nota_biologia_p3_tg) / 2
media2_biologia_p3 = (media1_biologia_p3 + nota_biologia_p3_aq + nota_biologia_p3_ab + nota_biologia_p3_sim) / 3

# Biologia P4
nota_biologia_p4_arf = 9.1
nota_biologia_p4_ab = 7.5
nota_biologia_p4_aq = 3.0
nota_biologia_p4_rec = 1.0
nota_biologia_p4_sim = 5.3
nota_biologia_p4_tg = 6.5
nota_biologia_p4_ap1 = 0.7

media1_biologia_p4 = (nota_biologia_p4_ap1 + nota_biologia_p4_tg ) / 2
media2_biologia_p4 = (media1_biologia_p4 + nota_biologia_p4_aq + nota_biologia_p4_ab + nota_biologia_p4_sim + nota_biologia_p4_arf) / 4
media3_biologia_p4 = media2_biologia_p4 + nota_biologia_p4_rec

# Ciências Naturais
nota_cn_p1_itf = 9.5

nota_cn_p2_itf = 9.5

nota_cn_p3_itf = 8.0

nota_cn_p4_itf = 10.0

# Educação Física P1
nota_edf_p1_aq = 2.3
nota_edf_p1_efe = 6.0

media1_edf_p1 = nota_edf_p1_aq + nota_edf_p1_efe

#Educação Física P2
nota_edf_p2_aq = 2.3
nota_edf_p2_efe = 6.1

media1_edf_p2 = nota_edf_p2_aq + nota_edf_p2_efe

#Educação Física P3
nota_edf_p3_aq = 2.3
nota_edf_p3_efe = 6.3

media1_edf_p3 = nota_edf_p3_aq + nota_edf_p3_efe

#Educação Física P4
nota_edf_p4_aq = 2.4
nota_edf_p4_efe = 6.0

media1_edf_p4 = nota_edf_p4_aq + nota_edf_p4_efe  

# Física P1
nota_fisica_p1_ab = 6.5
nota_fisica_p1_aq = 2.0
nota_fisica_p1_ti = 6.5
nota_fisica_p1_ap1 = 4.0

media1_fisica_p1 = (nota_fisica_p1_ap1 + nota_fisica_p1_ti ) / 2
media2_fisica_p1 = (media1_fisica_p1 + nota_fisica_p1_aq + nota_fisica_p1_ab) / 2

# Física P2
nota_fisica_p2_ab = 5.2
nota_fisica_p2_aq = 1.4
nota_fisica_p2_ti = 5.5
nota_fisica_p2_ap1 = 2.0
nota_fisica_p2_sim = 4.8
nota_fisica_p2_tg = 6.7

media1_fisica_p2 = (nota_fisica_p2_ap1 + nota_fisica_p2_ti + nota_fisica_p2_tg) / 3
media2_fisica_p2 = (media1_fisica_p2 + nota_fisica_p2_aq + nota_fisica_p2_ab +  nota_fisica_p2_sim) / 3

# Física P3
nota_fisica_p3_ab = 10.0
nota_fisica_p3_aq = 2.1
nota_fisica_p3_ap1 = 6.0
nota_fisica_p3_sim = 5.3
nota_fisica_p3_tg = 6.7

media1_fisica_p3 = (nota_fisica_p3_ap1 + nota_fisica_p3_tg) / 2
media2_fisica_p3 = (media1_fisica_p3 + nota_fisica_p3_aq + nota_fisica_p3_ab +  nota_fisica_p3_sim) / 3

# Física P4
nota_fisica_p4_arf = 9.1
nota_fisica_p4_ab = 2.0
nota_fisica_p4_aq = 2.2
nota_fisica_p4_ap1 = 1.0
nota_fisica_p4_sim = 5.3
nota_fisica_p4_tg = 6.8

media1_fisica_p4 = (nota_fisica_p4_ap1 + nota_fisica_p4_tg) / 2
media2_fisica_p4 = (media1_fisica_p4 + nota_fisica_p4_aq + nota_fisica_p4_ab +  nota_fisica_p4_sim + nota_fisica_p4_arf) / 4

# Início
print("=== PORTAL DO ALUNO ===")

# Informações 2
nome = input("Nome: ").lower()
senha = input("Senha: ")

# Cadastro
while nome != aluno_nome.lower() or senha != aluno_senha:
    print("\nAcesso negado, tente novamente.")
    nome = input("Nome: ").lower()
    senha = input("Senha: ")

# Informações
print(f"\nNome: {aluno_nome}")
print(f"Turma: {aluno_turma}\n")

# Matérias
print("=== MATÉRIAS ===")
while True:
    print("1 - Biologia\n2 - Ciências Naturais\n3 - Educação Física\n4 - Física\n0 - Sair")
    materia = input("\nEscolha uma opção: ")

# Matéria Biologia
    if materia == "1":
        while True:
            print("=== PERÍODOS ===\n")
            print("\n1 - 1º Período\n2 - 2º Período\n3 - 3º Período\n4 - 4º Período\n0 - Voltar")        
            periodo = input("Escolha uma opção: ")

# Perído 1
            if periodo == "1":
                print("\n=== NOTAS DE BIOLOGIA 1º PERÍODO ===")
                print(f"Avaliação Bimestral: {nota_biologia_p1_ab}/10.0\nMicrociclo: {nota_biologia_p1_ap1}/7.0\nAvaliação Qualitativa: {nota_biologia_p1_aq}/3.0\nTrabalho individual: {nota_biologia_p1_ti}/7.0\nTrabalho em Grupo: {nota_biologia_p1_tg}/7.0")
                print(f"\nMédia: {media2_biologia_p1:.1f}")

                if media2_biologia_p1 >= 7:
                    print("Situação: Aprovado(a)\n")

                else:
                    print("Situação: Recuperação\n")

# Período 2
            elif periodo == "2":
                print("\n=== NOTAS DE BIOLOGIA 2º PERÍODO ===")
                print(f"Avaliação Bimestral: {nota_biologia_p2_ab}/10.0\nSimulado: {nota_biologia_p2_sim}/10\nMicrociclo: {nota_biologia_p2_ap1}/7.0\nAvaliação Qualitativa: {nota_biologia_p2_aq}/3.0\nTrabalho individual: {nota_biologia_p2_ti}/7.0\nTrabalho em Grupo: {nota_biologia_p2_tg}/7.0")
                print(f"\nMédia: {media2_biologia_p2:.1f}")
                
                if media2_biologia_p2 >= 7:
                    print("Situação: Aprovado(a)\n")

                else:
                    print("Situação: Recuperação\n")

# Período 3
            elif periodo == "3":
                print("\n=== NOTAS DE BIOLOGIA 3º PERÍODO ===")
                print(f"Avaliação Bimestral: {nota_biologia_p3_ab}/10.0\nSimulado: {nota_biologia_p3_sim}/10\nMicrociclo: {nota_biologia_p3_ap1}/7.0\nAvaliação Qualitativa: {nota_biologia_p3_aq}/3.0\nTrabalho em Grupo: {nota_biologia_p3_tg}/7.0")
                print(f"\nMédia: {media2_biologia_p3:.1f}")
                
                if media2_biologia_p3 >= 7:
                    print("Situação: Aprovado(a)\n")

                else:
                    print("Situação: Recuperação\n")

# Período 4
            elif periodo == "4":
                print("\n=== NOTAS DE BIOLOGIA 4º PERÍODO ===")
                print(f"Arfec: {nota_biologia_p4_arf}/10.0\nAvaliação Bimestral: {nota_biologia_p4_ab}/10.0\nSimulado: {nota_biologia_p4_sim}/10\nMicrociclo: {nota_biologia_p4_ap1}/7.0\nAvaliação Qualitativa: {nota_biologia_p4_aq}/3.0\nTrabalho em Grupo: {nota_biologia_p4_tg}/7.0\nRecuperação: {nota_biologia_p4_rec}/1.0")
                print(f"\nMédia: {media3_biologia_p4:.1f}")
                
                if media3_biologia_p4 >= 7:
                    print("Situação: Aprovado(a)\n")

                else:
                    print("Situação: Recuperação\n")

# Período Voltar
            elif periodo == "0":
                print("\nVoltando ao menu de matérias")
                break

# Período Inválido
            else:
                print("\nOpção inválida, tente novamente.")

# Matéria Ciências Naturais
    elif materia == "2":
        while True:
            print("=== PERÍODOS ===\n")
            print("\n1 - 1º Período\n2 - 2º Período\n3 - 3º Período\n4 - 4º Período\n0 - Voltar")
            periodo = input("Escolha uma opção: ")

# Período 1
            if periodo == "1":
                print("\n=== NOTAS DE CIÊNCIAS NATURAIS 1º PERÍODO ===\n")
                print(f"Itinerário Formativo: {nota_cn_p1_itf}/10.0")
                
                if nota_cn_p1_itf >= 7:
                    print("Situação: Aprovado(a)\n")

                else:
                    print("Situação: Recuperação\n")

# Período 2
            elif periodo == "2":
                print("\n=== NOTAS DE CIÊNCIAS NATURAIS 2º PERÍODO ===")
                print(f"Itinerário Formativo: {nota_cn_p2_itf}/10.0")
                
                if nota_cn_p2_itf >= 7:
                    print("Situação: Aprovado(a)\n")

                else:
                    print("Situação: Recuperação\n")

# Período 3        
            elif periodo == "3":
                print("\n=== NOTAS DE CIÊNCIAS NATURAIS 3º PERÍODO ===")
                print(f"Itinerário Formativo: {nota_cn_p3_itf}/10.0")
                
                if nota_cn_p3_itf >= 7:
                    print("Situação: Aprovado(a)\n")

                else:
                    print("Situação: Recuperação\n")

# Período 4        
            elif periodo == "4":
                print("\n=== NOTAS DE CIÊNCIAS NATURAIS 4º PERÍODO ===")
                print(f"Itinerário Formativo: {nota_cn_p4_itf}/10.0")
                
                if nota_cn_p4_itf >= 7:
                    print("Situação: Aprovado(a)\n")

                else:
                    print("Situação: Recuperação\n")

# Período Voltar
            elif periodo == "0":
                print("\nVoltando ao menu de matérias")
                break
        
# Período Inválido
            else:
                print("\nOpção inválida, tente novamente.")

# Matéria Educação Física
    elif materia == "3":
        while True:
            print("=== PERÍODOS ===\n")
            print("\n1 - 1º Período\n2 - 2º Período\n3 - 3º Período\n4 - 4º Período\n0 - Voltar")        
            periodo = input("Escolha uma opção: ")

# Período 1
            if periodo == "1":
                print("\n=== NOTAS DE EDUCAÇÃO FÍSICA 1º PERÍODO ===")
                print(f"Avaliação Qualitativa: {nota_edf_p1_aq}/3.0\nEFE: {nota_edf_p1_efe}/7.0")
                print(f"\nMédia: {media1_edf_p1:.1f}")
                
                if media1_edf_p1 >= 7:
                    print("Situação: Aprovado(a)\n")

                else:
                    print("Situação: Recuperação\n")

# Período 2
            elif periodo == "2":
                print("\n=== NOTAS DE EDUCAÇÃO FÍSICA 2º PERÍODO ===")
                print(f"Avaliação Qualitativa: {nota_edf_p2_aq}/3.0\nEFE: {nota_edf_p2_efe}/7.0")
                print(f"\nMédia: {media1_edf_p2:.1f}")
                
                if media1_edf_p2 >= 7:
                    print("Situação: Aprovado(a)\n")

                else:
                    print("Situação: Recuperação\n")

# Período 3
            elif periodo == "3":
                print("\n=== NOTAS DE EDUCAÇÃO FÍSICA 3º PERÍODO ===")
                print(f"Avaliação Qualitativa: {nota_edf_p3_aq}/3.0\nEFE: {nota_edf_p3_efe}/7.0")
                print(f"\nMédia: {media1_edf_p3:.1f}")
                
                if media1_edf_p3 >= 7:
                    print("Situação: Aprovado(a)\n")

                else:
                    print("Situação: Recuperação\n")

# Período 4
            elif periodo == "4":
                print("\n=== NOTAS DE EDUCAÇÃO FÍSICA 4º PERÍODO ===")
                print(f"Avaliação Qualitativa: {nota_edf_p4_aq}/3.0\nEFE: {nota_edf_p4_efe}/7.0")
                print(f"\nMédia: {media1_edf_p4:.1f}")
                
                if media1_edf_p4 >= 7:
                    print("Situação: Aprovado(a)\n")

                else:
                    print("Situação: Recuperação\n")

# Período Voltar
            elif periodo == "0":
                print("\nVoltando ao menu de matérias")
                break                  

# Período Inválido
            else:
                print("\nOpção inválida, tente novamente.")

# Materia Física
    elif materia == "4":
        while True:
            print("=== PERÍODOS ===\n")
            print("\n1 - 1º Período\n2 - 2º Período\n3 - 3º Período\n4 - 4º Período\n0 - Voltar")        
            periodo = input("Escolha uma opção: ")

# Perído 1
            if periodo == "1":
                print("\n=== NOTAS DE FÍSICA 1º PERÍODO ===")
                print(f"Avaliação Bimestral: {nota_fisica_p1_ab}/10.0\nMicrociclo: {nota_fisica_p1_ap1}/7.0\nAvaliação Qualitativa: {nota_fisica_p1_aq}/3.0\nTrabalho individual: {nota_fisica_p1_ti}/7.0")
                print(f"\nMédia: {media2_fisica_p1:.1f}")

                if media2_fisica_p1 >= 7:
                    print("Situação: Aprovado(a)\n")

                else:
                    print("Situação: Recuperação\n")

# Período 2
            elif periodo == "2":
                print("\n=== NOTAS DE FÍSICA 2º PERÍODO ===")
                print(f"Avaliação Bimestral: {nota_fisica_p2_ab}/10.0\nSimulado: {nota_fisica_p2_sim}/10\nMicrociclo: {nota_fisica_p2_ap1}/7.0\nAvaliação Qualitativa: {nota_fisica_p2_aq}/3.0\nTrabalho individual: {nota_fisica_p2_ti}/7.0\nTrabalho em Grupo: {nota_fisica_p2_tg}/7.0")
                print(f"\nMédia: {media2_fisica_p2:.1f}")
                
                if media2_fisica_p2 >= 7:
                    print("Situação: Aprovado(a)\n")

                else:
                    print("Situação: Recuperação\n")

# Período 3
            elif periodo == "3":
                print("\n=== NOTAS DE FÍSICA 3º PERÍODO ===")
                print(f"Avaliação Bimestral: {nota_fisica_p3_ab}/10.0\nSimulado: {nota_fisica_p3_sim}/10\nMicrociclo: {nota_fisica_p3_ap1}/7.0\nAvaliação Qualitativa: {nota_fisica_p3_aq}/3.0\nTrabalho em Grupo: {nota_fisica_p3_tg}/7.0")
                print(f"\nMédia: {media2_fisica_p3:.1f}")
                
                if media2_fisica_p3 >= 7:
                    print("Situação: Aprovado(a)\n")

                else:
                    print("Situação: Recuperação\n")

# Período 4
            elif periodo == "4":
                print("\n=== NOTAS DE FÍSICA 4º PERÍODO ===")
                print(f"Arfec: {nota_fisica_p4_arf}/10.0\nAvaliação Bimestral: {nota_fisica_p4_ab}/10.0\nSimulado: {nota_fisica_p4_sim}/10\nMicrociclo: {nota_fisica_p4_ap1}/7.0\nAvaliação Qualitativa: {nota_fisica_p4_aq}/3.0\nTrabalho em Grupo: {nota_fisica_p4_tg}/7.0")
                print(f"\nMédia: {media2_fisica_p4:.1f}")
                
                if media2_fisica_p4 >= 7:
                    print("Situação: Aprovado(a)\n")

                else:
                    print("Situação: Recuperação\n")

# Período Voltar
            elif periodo == "0":
                print("\nVoltando ao menu de matérias")
                break

# Período Inválido
            else:
                print("\nOpção inválida, tente novamente.")

# Matéria Sair
    elif materia == "0":
        print("\nVocê saiu do PORTAL DE NOTAS")
        break  

# Matéria Inválida
    else:
        print("\nOpção inválida, tente novamente.")
