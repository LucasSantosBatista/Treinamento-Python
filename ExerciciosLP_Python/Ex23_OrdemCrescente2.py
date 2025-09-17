# Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não

print('Bem vindo ao Sistema Ordem Crescente')

n1: int = int(input('Digite um valor qualquer: '))

n2: int = int(input(f'Digite um valor maior que {n1}: '))

n3: int = int(input(f'Digite um valor maior que {n2}: '))

n4: int = int(input(f'Digite um valor qualquer: '))

if n4 < n1:
    print(f"Ordem Crescente: {n4}, {n1}, {n2}, {n3}")
elif n4 < n2:
    print(f"Ordem Crescente: {n1}, {n4}, {n2}, {n3}")
elif n4 < n3:
    print(f"Ordem Crescente: {n1}, {n2}, {n4}, {n3}")
else:
    print(f"Ordem Crescente: {n1}, {n2}, {n3}, {n4}")
