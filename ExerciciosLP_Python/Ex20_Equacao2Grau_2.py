# Receba 3 coeficientes A, B, e C de uma equação do 2º grau da fórmula
# AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.
import math

print("Bem vindo ao Calculo de Equação de 2º grau")

A: int = int(input('=> Ax² + Bx + C = 0\nDigite o valor de A: '))

B: int = int(input('=> ' + str(A) + 'x² + Bx + C = 0\nDigite o valor de B: '))

C: int = int(input('=> ' +str(A) + 'x² + ' + str(B) + 'x + C = 0\nDigite o valor de C: '))

print('Equação: ' + str(A) + 'x² + ' + str(B) + 'x + ' + str(C) + ' = 0')

Delta: float = (math.pow(B, 2)) - (4 * A * C)

print(f'Delta: {B}² - 4 * {A} * {C} = {Delta}')

if Delta > 0:
    # Duas raízes reais
    R1 = (-B + math.sqrt(Delta)) / (2 * A)
    R2 = (-B - math.sqrt(Delta)) / (2 * A)
    print(f'Existem duas raízes reais: x₁ = {R1:.2f} e x₂ = {R2:.2f}')

elif Delta == 0:
    # Uma raiz real (dupla)
    R = -B / (2 * A)
    print(f'Existe uma raiz real (dupla): x = {R:.2f}')

else:
    print("Não há raízes reais")