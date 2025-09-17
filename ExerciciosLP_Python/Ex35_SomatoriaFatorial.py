# Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!

print("Bem vindo a Somatoria Fatorial")

n = int(input("Digite um valor para a somatória S = 1 + 1/1! + 1/2! + ... + 1/N!: "))

S = 1.0  # Começa com 1 (1/0!)

fatorial = 1  # variável para ir acumulando o fatorial

for k in range(1, n + 1):
    fatorial *= k       # atualiza o fatorial para k!
    S += 1 / fatorial   # soma 1/k!

print(f"Resultado com N = {n}, S = {S:.3f}")