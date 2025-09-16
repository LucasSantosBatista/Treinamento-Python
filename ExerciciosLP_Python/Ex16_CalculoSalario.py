# Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto
# e o número de descendentes. Calcule o salário que serão as horas trabalhadas
# x o valor por hora. Calcule o salário líquido (= Salário Bruto – desconto).
# A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o salário a receber.

print("Bem vindo ao Calculo de Salario")

horasTrabalhadas: int = int(input("Digite a quantidade de horas trabalhadas: "))

valorHora: int = int(input("Digite o valor por hora: R$ "))

salarioBruto: float = valorHora * horasTrabalhadas

percentualDesconto: int = int(input("Digite o percentual de desconto (%): "))
decimalDesconto: float = percentualDesconto / 100

salarioLiquido: float = salarioBruto - (salarioBruto * decimalDesconto)

numDescendentes: int = int(input("Digite a quantidade de descendentes: "))

salarioLiquido += numDescendentes * 100

print("Horas trabalhadas: " + str(horasTrabalhadas) + " horas")
print("Valor por hora: R$ " + str(valorHora) +"/h")
print("Desconto: " + str(percentualDesconto) + "%")
print("Salario bruto: R$ " + str(f"{salarioBruto:.2f}"))
print("Numero de descendentes: " + str(numDescendentes))
print("Salario liquido: R$ " + str(f"{salarioLiquido:.2f}"))
