# Receba a quantidade de alimento em quilos.
# Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.

print('Bem vindo ao Calculo de Consumo')

alimento: int = int(input('Digite a quantidade de alimento (em kg), sabendo que será consumido 50g por dia: '))

alimento *= 1000

dias = 0

while alimento > 0:
    dias += 1
    print('Dia ' + str(dias) + ': comeu 50g e sobrou ' + str(alimento) + 'g')
    alimento -= 50
