# Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.

print("Bem vindo ao Calculo de Divisiveis")

n: int = int(input("Digite um número inteiro para verificar se é divisivel por 2 ou 3: "))

if n % 2 == 0:
    if n % 3 == 0:
        print(f"{n} é divisivel por 2 e por 3")
    else:
        print(f"{n} é divisivel apenas por 2")
elif n % 3 == 0:
    print(f"{n} é divisivel apenas por 3")
else:
    print(f"{n} não é divisivel por 2 nem 3")