# Receba o salário de um funcionário e mostre o novo salário com reajuste de 15%.

print('Bem vindo ao Sistema de Reajuste')
salario = float(input("Digite o valor do salario: "))

salario = salario * 1.15
fsalario = f"{salario:.2f}"

print("Novo salario com reajuste de 15%: R$ " + fsalario)