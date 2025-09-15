# Receba os valores do comprimento, largura e altura de um paralelepípedo.
# Calcule e mostre seu volume.

print('Bem vindo ao Calculo de Volume do Paralelepipedo')

comprimento: float = float(input('Digite o comprimento(cm): '))
largura: float = float(input('Digite a largura (cm): '))
altura: float = float(input('Digite a para altura (cm): '))

volume: float = comprimento * largura * altura

print('Volume do paralelepipedo = ' + str(f"{volume:.2f}" + 'cm3'))