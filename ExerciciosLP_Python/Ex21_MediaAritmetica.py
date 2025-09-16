# Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética.
# Mostre a mensagem de acordo com a média:
#     a. Se a média for >= 6,0 exibir “APROVADO”;
#     b. Se a média for >= 3,0 ou < 6,0 exibir “EXAME”;
#     c. Se a média for < 3,0 exibir “RETIDO”.

print("Bem vindo ao Calculo de Notas")

n1: float = float(input("Digite a nota do primeiro bimestre do aluno: "))
n2: float = float(input("Digite a nota do segundo bimestre do aluno: "))
n3: float = float(input("Digite a nota do terceiro bimestre do aluno: "))
n4: float = float(input("Digite a nota do quarto bimestre do aluno: "))

media: float = (n1 + n2 + n3 + n4) / 4

if media >= 6:
    print(f"Nota 1: {n1:.1f}\n"
          f"Nota 2: {n2:.1f}\n"
          f"Nota 3: {n3:.1f}\n"
          f"Nota 4: {n4:.1f}\n"
          f"Média: {media:.1f}\n"
          f"Situação Final: APROVADO")
elif media >= 3 and media < 6:
    print(f"Nota 1: {n1:.1f}\n"
          f"Nota 2: {n2:.1f}\n"
          f"Nota 3: {n3:.1f}\n"
          f"Nota 4: {n4:.1f}\n"
          f"Média: {media:.1f}\n"
          f"Situação Final: EXAME DE RECUPERAÇÃO")
else:
    print(f"Nota 1: {n1:.1f}\n"
          f"Nota 2: {n2:.1f}\n"
          f"Nota 3: {n3:.1f}\n"
          f"Nota 4: {n4:.1f}\n"
          f"Média: {media:.1f}\n"
          f"Situação Final: RETIDO")