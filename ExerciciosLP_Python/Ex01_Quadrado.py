# Coletar o valor do lado de um quadrado, calcular sua área e apresentar o resultado.
import math

lado = float(input("Digite o valor do lado do quadrado: "))
area: float = math.pow(lado, 2)

print("Área do quadrado: " + str(area) + "cm2")
