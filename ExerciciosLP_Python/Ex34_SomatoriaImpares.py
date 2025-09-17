# Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e
# mostre o resultado da somatória dos números ímpares entre esses valores.

print("Bem vindo a Somatoria de Impares")

n1: int = int(input("Digite o primeiro valor: "))
n2: int = int(input("Digite o segundo valor: "))

S: int = 0

if n1 > n2:
    for i in range(n2, n1, 1):
        if i % 2 != 0:
            S += i
    print(f"Soma dos valores impares entre {n2} e {n1} = {S}")
else:
    for i in range(n1, n2, 1):
        if i % 2 != 0:
            S += i
    print(f"Soma dos valores impares entre {n1} e {n2} = {S}")
