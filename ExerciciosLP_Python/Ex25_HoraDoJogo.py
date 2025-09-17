# Receba a hora de início e de final de um jogo (HH,MM) sabendo que o
# tempo máximo é de 24 horas e pode começar num dia e terminar noutro.

print("Bem vindo ao Jogo")

horaInicio = int(input("Hora de início (0-23): "))
minutoInicio = int(input("Minuto de início (0-59): "))
horaFim = int(input("Hora de fim (0-23): "))
minutoFim = int(input("Minuto de fim (0-59): "))

# Converte horas e minutos para minutos totais
inicioTotal = horaInicio * 60 + minutoInicio
fimTotal = horaFim * 60 + minutoFim

# Se o fim for menor ou igual ao início, significa que passou da meia-noite
if fimTotal <= inicioTotal:
        fimTotal += 24 * 60  # adiciona 24 horas em minutos

# Calcula duração do jogo
duracao = fimTotal - inicioTotal
duracaoHoras = duracao // 60
duracaoMinutos = duracao % 60

print(f"Horário do inicio de jogo: {horaInicio}:{minutoInicio} hrs")
print(f"Horário do fim de jogo: {horaFim}:{minutoFim} hrs")
print(f"Duração do jogo: {duracaoHoras}:{duracaoMinutos} hrs")