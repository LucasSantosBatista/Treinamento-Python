# Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.

print("Bem vindo ao Calculo de Somatoria")

n: int = int(input("Digite um valor para a somatória S = 1 + 1/2 + 1/3 + ... + 1/N: "))

S: float = 0

for k in range(1,n + 1, 1):
    S += 1/k

print(f"Resultado com N = {n}, S = {S:.3f}")