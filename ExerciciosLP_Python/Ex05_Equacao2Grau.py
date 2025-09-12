# Receba os coeficientes A, B e C de uma equação do 2º grau
# (Ax²+Bx+C=0). Calcule e mostre as raízes reais (considerar que a equação possui 2 raízes).
# Nota:   (Ax² + Bx + C = 0) = Equação do segundo grau.
#         (Δ = B² – 4*A*C)  = Calculo do delta.
#         (x = (– b ± √∆/2))    = Calculo das raízes.
# Nota 2: Teste (2x² – 8x + 6 = 0) (S = {3, 1})
import math

print('Bem vindo ao cálculo de equação do 2º grau')

A: int = int(input('=> Ax² + Bx + C = 0\nDigite o valor de A: '))

B: int = int(input('=> ' + str(A) + 'x² + Bx + C = 0\nDigite o valor de B: '))

C: int = int(input('=> ' +str(A) + 'x² + ' + str(B) + 'x + C = 0\nDigite o valor de C: '))

Delta: float = (math.pow(B, 2)) - (4 * A * C)

print('Equação: ' + str(A) + 'x² + ' + str(B) + 'x + ' + str(C) + ' = 0')

R1: float = (-B + math.sqrt(Delta)) / (2 * A)
R2: float = (-B - math.sqrt(Delta)) / (2 * A)

fR1 = f"{R1:.0f}"
fR2 = f"{R2:.0f}"

print('Resultado: S = {' + fR1 + ', ' + fR2 + '}')