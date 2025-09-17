# Receba um número. Calcule e mostre os resultados da tabuada desse número.

print("Bem vindo ao Sistema de Tabuada")

n: int = int(input("Digite um número para a tabuada: "))

print(f"Tabuada do {n}")
for i in range(0, 10, 1):
    print(f"{n} x {i} = {n * i}")