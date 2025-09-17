# Receba o tipo de investimento (1 = poupança e 2 = renda fixa)
# e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a
# poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.

print("Bem vindo ao Sistema de Investimento")

valorInvestimento: float = 0

opt: int = 0
while opt != 1 and opt != 2:
    opt = int(input("Escolha o tipo de investimento: 1- Poupança | 2- Renda Fixa:\n"))

    if opt == 1:
        valorInvestimento = float(input("Digite o valor que deseja investir na poupança (3% a. m.): R$ "))
        valorInvestimento *= 1 + 0.03
    elif opt == 2:
        valorInvestimento = float(input("Digite o valor que deseja investir na renda fixa (5% a. m.): R$ "))
        valorInvestimento *= 1 + 0.05
    else:
        print("Entrada invalida! Tente novamente")


print(f"Valor após 30 dias: R$ {valorInvestimento:.2f}")