# Receba 2 valores reais. Calcule e mostre o maior deles.

print("Bem vindo ao Calculo de Maior Valor Real")

n1: float = float(input("Digite o primeiro valor: "))
n2: float = float(input("Digite o segundo valor: "))

if n1 > n2:
    print(f"{n1:.2f} é maior valor")
elif n1 < n2:
    print(f"{n2:.2f} é maior valor")
else:
    print(f"Os valores são iguais!")