# Receba o raio de uma circunferência.
# Calcule e mostre o comprimento da circunferência.
import math

print('Bem vindo ao Calculo de Comprimento da Circunferencia')

raio: float = float(input('Digite o valor de raio: '))

comprimento: float = 2*math.pi*raio

print('Raio = ' + str(raio) + 'cm | Comprimento = ' + str(f"{comprimento:.1f}" + ' cm'))