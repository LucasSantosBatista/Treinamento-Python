# Receba os 2 números inteiros. Calcule e mostre a soma dos quadrados
import math

print('Bem vindo a Soma de Quadrados')

A: int = int(input('Digite o valor de A: '))
B: int = int(input('Digite o valor de B: '))

powA: int = int(math.pow(A, 2))
powB: int = int(math.pow(B, 2))

resultado = powA + powB

print('A² + B² = ' + str(resultado))