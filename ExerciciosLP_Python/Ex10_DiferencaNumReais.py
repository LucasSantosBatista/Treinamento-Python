# Receba 2 números reais. Calcule e mostre a diferença desses valores.

print('Bem vindo ao Calculo de Números Reais')

n1: int = int(input('Digite o primeiro valor: '))
n2: int = int(input('Digite o segundo valor: '))

resultado: int

if n1 > n2:
    resultado = n1 - n2
else:
    resultado = n2 - n1

print('Diferença entre ' + str(n1) + ' e ' + str(n2) + ' = ' +str(resultado))