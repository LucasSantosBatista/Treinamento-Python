# Receba 2 números inteiros. Verifique e
# mostre se o maior número é múltiplo do menor.

print("Bem vindo ao Sistema de Multiplo")

n1: int = int(input("Digite o primeiro valor: "))
n2: int = int(input("Digite o segundo valor: "))

if n1 > n2:
    if n1 % n2 == 0:
        print(f"{n1} é multiplo de {n2}")
    else:
        print(f"{n1} não é multiplo de {n2}")
elif n2 > n1:
    if n2 % n1 == 0:
        print(f"{n2} é multiplo de {n1}")
    else:
        print(f"{n2} não é multiplo de {n1}")
else:
    print("Os valores são iguais!")