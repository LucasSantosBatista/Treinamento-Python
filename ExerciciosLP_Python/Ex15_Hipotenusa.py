# Receba os valores de 2 catetos de um triângulo retângulo.
# Calcule e mostre a hipotenusa.
import math

print("Bem vindo ao Calculo de Hipotenusa")

c1: int = int(input("Digite o valor do primeiro cateto: "))
c2: int = int(input("Digite o valor do segundo cateto: "))

h: int = int((math.pow(c1, 2) + math.pow(c2, 2))/2)

print("Valor do hipotenusa: " + str(h) + "²")