# Receba o número de voltas, a extensão do circuito (em metros)
# e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.

print("Bem-vindo à Corrida")

numeroVoltas: int = int(input("Digite o número de voltas: "))
tamanhoCircuito: int = int(input("Digite o tamanho do circuito (em metros): "))
tempoDuracao: int = int(input("Digite o tempo de duração (em minutos): "))

distanciaCircuito: float = tamanhoCircuito * numeroVoltas  # em metros

duracaoCircuito: float = tempoDuracao / 60  # em horas

velocidadeMedia: float = (distanciaCircuito / 1000) / duracaoCircuito  # em km/h

print(f"\nDistância Total do Circuito: {distanciaCircuito} metros")
print(f"Duração: {duracaoCircuito:.2f} horas")
print(f"Velocidade média: {velocidadeMedia:.2f} km/h")
