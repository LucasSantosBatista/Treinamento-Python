# Receba os valores em x e y. Efetua a troca de seus valores e mostre seus
# conteúdos.
import time

print('Bem vindo ao Sistema Troca de Valores')

x: int = int(input('Digite o valor para x: '))
y: int = int(input('Digite o valor para y: '))

print('Valores antes da troca: x = ' + str(x) + ' | y = ' + str(y))

time.sleep(1)

aux: int = x
x = y
y = aux


print('Valores após a troca: x = ' + str(x) + ' | y = ' + str(y))