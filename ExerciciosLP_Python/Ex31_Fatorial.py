# Receba um número inteiro. Calcule e mostre o seu fatorial.

print("Bem vindo ao Calculo de Fatorial")

n: int = int(input("Digite um valor para o fatorial: "))
resultado: int = 1

for i in range(n, 0, -1): # i = valor atual | range(inicio,fim,iteração)
    resultado *= i

print(f"N = {n} | Fatorial = {resultado}")