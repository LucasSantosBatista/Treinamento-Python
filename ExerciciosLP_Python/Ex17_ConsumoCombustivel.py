# Calcule a quantidade de litros gastos em uma
# viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média

print("Bem vindo ao Calculo de Gasto de Combustivel")

tempoPercurso: float = float(input("Digite o tempo do percurso (em horas): "))

velocidadeMedia: float = float(input("Digite a velocidade média (em km): "))

distanciaPercurso: float = velocidadeMedia * tempoPercurso

litrosGastos: float = distanciaPercurso / 12

print(f"Tempo do percurso: {tempoPercurso:.1f} hrs")
print(f"Velocidade média: {velocidadeMedia:.0f} km/h")
print(f"Distância do percurso: {distanciaPercurso:.1f} km")
print(f"Litros de combustível gastos na viagem: {litrosGastos:.1f} l")