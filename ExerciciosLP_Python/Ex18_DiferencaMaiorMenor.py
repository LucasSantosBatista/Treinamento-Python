# Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.

print("Bem vindo a Diferença Maior Menor")

n1: int = int(input("Digite o primeiro valor: "))
n2: int = int(input("Digite o segundo valor: "))

if n1 > n2:
    resultado = n1 - n2
    print(f"A diferença entre {n1} e {n2} é {resultado}")
elif n1 < n2:
    resultado = n2 - n1
    print(f"A diferença entre {n2} e {n1} é {resultado}")
else:
    print(f"Os valores são iguais!")