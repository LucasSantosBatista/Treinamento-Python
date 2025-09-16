# Receba 2 ângulos de um triângulo.
# Calcule e mostre o valor do 3º ângulo.

print("Bem vindo ao Calculo de Angulos")

a: int = int(input("Digite o primeiro angulo do triangulo: "))
b: int = int(input("Digite o segundo angulo do triangulo: "))

c = 180 - (a + b)

print("Valor do terceiro angulo: " + str(c) + "º" )
