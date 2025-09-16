# Receba 2 valores inteiros e diferentes.
# Mostre seus valores em ordem crescente.

print("Bem vindo ao Sistema de Ordem Crescente")

n1: int = int(input("Digite o primeiro valor: "))
n2: int = int(input("Digite o segundo valor: "))

if n1 == n2:
    print("Os valores são iguais!")
elif n1 > n2 :
    print(f"Valores em ordem crescente: {n2} => {n1} ")
else:
    print(f"Valores em ordem crescente: {n1} => {n2} ")