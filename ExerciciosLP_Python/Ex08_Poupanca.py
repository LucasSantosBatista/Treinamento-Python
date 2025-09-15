# Receba o valor de um depósito em poupança. Calcule e mostre o valor
# após 1 mês de aplicação sabendo que rende 1,3% a. m.

print('Bem vindo ao Sistema de Rendimento da Poupança')

valor: float = float(input("Digite o valor do depósito na poupança (rende 1,3% a. m.): R$ "))

rendimento: float = valor * 1.013

print('Valor após 1 mês: R$ ' + str(f"{rendimento:.2f}"))