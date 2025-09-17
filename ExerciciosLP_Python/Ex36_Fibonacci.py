# Receba um número inteiro. Calcule e mostre a série de Fibonacci
# até o seu N’nésimo termo.

print("Bem vindo ao Sistema Fibonacci")

n = int(input("Digite a quantidade de termos da sequência de Fibonacci que deseja: "))

a: int = 1
b: int = 1
ct: int = 0

while ct < n:
    print(a, end=' ')
    aux = a
    a = b
    b = aux + b
    ct += 1